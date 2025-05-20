# Importa BeautifulSoup para fazer scraping (extrair dados) de sites HTML
from bs4 import BeautifulSoup
# Requests serve para fazer requisições HTTP e baixar conteúdo da web
import requests
# Selenium permite controlar o navegador automaticamente
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Cabeçalhos para simular um navegador real (evita bloqueio por bots)
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5)...",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Faz uma requisição GET ao site de imóveis (uma cópia do Zillow para prática)
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
data = response.text  # Pega o HTML da página
soup = BeautifulSoup(data, "html.parser")  # Analisa o HTML

# Extrai todos os links dos imóveis usando seletor CSS
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
# Pega apenas os atributos "href" dos links (endereços das páginas)
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

# Extrai e limpa os endereços dos imóveis
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
# Remove quebras de linha e símbolos indesejados
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

# Extrai e limpa os preços dos imóveis
all_price_elements = soup.select(".PropertyCardWrapper span")
# Remove "/mo" e "+" (caso existam), e garante que só pega textos com $
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)

# --------------------------
# PARTE 2 – Preenchendo Formulário do Google com Selenium
# --------------------------

# Configura o navegador para continuar aberto após o script (útil para debug)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Itera por todos os imóveis encontrados
for n in range(len(all_links)):
    # Substitua aqui pelo link do SEU Google Form:
    driver.get("YOUR_GOOGLE_FORM_LINK_HERE")
    time.sleep(2)  # Espera a página carregar

    # Localiza os campos de texto no formulário com XPath
    address = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    # Preenche os campos com os dados raspados
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])

    # Clica no botão de "Enviar"
    submit_button.click()
