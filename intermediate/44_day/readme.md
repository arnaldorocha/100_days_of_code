# 🍪 Cookie Clicker Bot com Python + Selenium

Este projeto automatiza o famoso jogo [Cookie Clicker](http://orteil.dashnet.org/experiments/cookie/) utilizando o Selenium WebDriver. O bot clica automaticamente no cookie e compra os upgrades mais caros que puder a cada 5 segundos, por um total de 5 minutos.

---

## 📌 O que você vai aprender

- Automatizar interações com páginas web usando Selenium
- Usar seletores CSS para encontrar elementos
- Extrair e processar valores de texto
- Tomar decisões automáticas com base em valores lógicos

---

## 📦 Requisitos

- Python 3.x
- Google Chrome instalado
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com sua versão do Chrome
- Bibliotecas Python:

```bash
pip install selenium


🧠 Como o bot funciona — passo a passo
🔁 1. Inicialização e configuração do navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
Abre o navegador com uma opção que não fecha automaticamente ao fim do script (útil para depuração).

🌐 2. Acessando o site do jogo
driver.get("http://orteil.dashnet.org/experiments/cookie/")
Acessa o site oficial da versão de testes do Cookie Clicker.

🍪 3. Identificando elementos da página
cookie = driver.find_element(by=By.ID, value="cookie")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
Captura o cookie principal para clicar.

Obtém os IDs dos upgrades disponíveis na loja.

⏲️ 4. Definindo o tempo de execução
timeout = time.time() + 5      # Intervalo de 5 segundos entre checagens
five_min = time.time() + 60*5  # Tempo total de execução: 5 minutos

🤖 5. Loop principal do bot
while True:
    cookie.click()
O bot clica constantemente no cookie.

A cada 5 segundos:

🏪 a. Verifica os preços dos upgrades
all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
item_prices = [...]
Extrai os preços dos upgrades e converte para inteiros.

💸 b. Compara com o total de cookies atuais
money_element = driver.find_element(by=By.ID, value="money").text
cookie_count = int(money_element.replace(",", ""))
Verifica quantos cookies você tem no momento.

🛍️ c. Compra o melhor upgrade possível
if cookie_count > cost:
    # ...
driver.find_element(by=By.ID, value=to_purchase_id).click()
Compra o upgrade mais caro possível entre os que você pode pagar.

⏹️ 6. Finaliza após 5 minutos
if time.time() > five_min:
    cookie_per_s = driver.find_element(by=By.ID, value="cps").text
    print(cookie_per_s)
    break
Após 5 minutos, imprime a quantidade de cookies gerados por segundo (CPS) e encerra o bot.

📊 Exemplo de Saída
yaml
5400
7680
9200
Cookies por segundo: 72.4

⚠️ Observações
Pode haver pequenas variações nos seletores CSS caso o site da Billboard ou Cookie Clicker seja atualizado.

Este script foi feito para fins educacionais. Automatizar jogos reais ou com sistemas de monetização pode violar os termos de uso dos sites.

✅ Conclusão
Este bot é um excelente exercício para quem está aprendendo:

Automação de tarefas com Selenium

Manipulação de elementos web

Tomada de decisões baseadas em dados extraídos da web

