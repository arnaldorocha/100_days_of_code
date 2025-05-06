import requests
from twilio.rest import Client
import os

# --- Configurações ---
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Suas chaves de API (deixe como variáveis de ambiente para segurança)
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")     # Número Twilio (ex: "+1415...")
DEST_PHONE = os.environ.get("DEST_PHONE")         # Seu número (ex: "+55...")

# --- Endpoints ---
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# --- Etapa 1: Obter dados de ações ---
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

# --- Etapa 2: Calcular a diferença percentual ---
difference = yesterday_close - day_before_close
up_down = "🔺" if difference > 0 else "🔻"
percent_diff = round((abs(difference) / day_before_close) * 100)

# --- Etapa 3: Se variar mais de 5%, buscar notícias ---
if percent_diff >= 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    # --- Etapa 4: Enviar via SMS ---
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in articles:
        message_body = f"{STOCK}: {up_down}{percent_diff}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=DEST_PHONE
        )
        print(f"Mensagem enviada: {message.status}")
else:
    print(f"{STOCK}: Mudança de {percent_diff}%. Sem alerta necessário.")
