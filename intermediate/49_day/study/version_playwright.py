from bs4 import BeautifulSoup
import requests
import asyncio
from playwright.async_api import async_playwright

# Cabeçalhos para simular acesso por um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5)...",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Raspagem de dados com BeautifulSoup
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Lista de links para os imóveis
all_links = [link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]

# Lista de endereços limpos
all_addresses = [address.get_text().replace(" | ", " ").strip()
                 for address in soup.select(".StyledPropertyCardDataWrapper address")]

# Lista de preços limpos
all_prices = [price.get_text().replace("/mo", "").split("+")[0]
              for price in soup.select(".PropertyCardWrapper span") if "$" in price.text]

# Link do seu formulário do Google
GOOGLE_FORM_URL = "https://YOUR_FORM_URL_HERE"

# Função assíncrona para preencher o formulário
async def fill_form():
    async with async_playwright() as p:
        # Abre o navegador (modo visível: headless=False)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Itera por todos os imóveis e preenche o formulário
        for i in range(len(all_links)):
            await page.goto(GOOGLE_FORM_URL)
            await page.wait_for_timeout(2000)

            # Digita nos campos (mude os seletores conforme seu formulário real)
            await page.locator('input[type="text"]').nth(0).fill(all_addresses[i])
            await page.locator('input[type="text"]').nth(1).fill(all_prices[i])
            await page.locator('input[type="text"]').nth(2).fill(all_links[i])

            # Clica no botão de envio
            await page.locator('div[role="button"]').click()

            # Aguarda um pouco antes de passar para o próximo
            await page.wait_for_timeout(2000)

        await browser.close()

# Executa o código assíncrono
asyncio.run(fill_form())
