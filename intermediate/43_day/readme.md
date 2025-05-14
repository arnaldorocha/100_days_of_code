# 🔍 O que o código faz, passo a passo

## 📦 Importa bibliotecas necessárias:

- `BeautifulSoup` e `requests`: Para fazer scraping da página da Amazon.
- `smtplib`: Para enviar e-mails.
- `os` e `dotenv`: Para usar variáveis de ambiente com segurança (como email e senha).

---

## ⚙️ Carrega variáveis do arquivo `.env`:

```python
load_dotenv()



🔍 O que o código faz, passo a passo:
Importa bibliotecas necessárias:

BeautifulSoup e requests: Para fazer scraping da página da Amazon.

smtplib: Para enviar e-mails.

os e dotenv: Para usar variáveis de ambiente com segurança (como email e senha).

Carrega variáveis do arquivo .env:

load_dotenv()
Essas variáveis devem conter dados como:

dotenv

EMAIL_ADDRESS=seuemail@exemplo.com
EMAIL_PASSWORD=sua_senha_segura
SMTP_ADDRESS=smtp.seuprovedor.com
Define o produto a ser monitorado (nesse caso, uma Instant Pot da Amazon):


url = "https://www.amazon.com/dp/B075CYMYK6?..."
Envia uma requisição HTTP com cabeçalhos simulando um navegador real (para evitar bloqueios da Amazon):

response = requests.get(url, headers=header)
Usa o BeautifulSoup para parsear o HTML:

soup = BeautifulSoup(response.content, "html.parser")
Extrai o preço do produto:

price = soup.find(class_="a-offscreen").get_text()
price_as_float = float(price.split("$")[1])
Extrai o título do produto:

title = soup.find(id="productTitle").get_text().strip()
Verifica se o preço é menor do que um limite definido (ex: $70):


if price_as_float < BUY_PRICE:
Se for, envia um e-mail para avisar:


connection.sendmail(...)
📧 Exemplo de mensagem de e-mail:
csharp


Assunto: Amazon Price Alert!

Instant Pot is on sale for $68.99!
https://www.amazon.com/dp/B075CYMYK6

✅ Resumo:
Esse código é um bot de rastreamento de preços com notificação por e-mail. Ideal para:

Acompanhar promoções na Amazon.

Automatizar alertas de compras.

Treinar scraping + automação.