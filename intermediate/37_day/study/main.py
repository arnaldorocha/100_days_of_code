# Importa bibliotecas necessárias
import requests  # Para fazer chamadas HTTP (usado para consumir APIs)
from datetime import datetime  # Para capturar data e hora atuais
import os  # Para acessar variáveis de ambiente de forma segura

# Dados pessoais usados para o cálculo de calorias pela API da Nutritionix
GENDER = "male"  # Sexo da pessoa que fez os exercícios
WEIGHT_KG = 84  # Peso corporal em kg
HEIGHT_CM = 180  # Altura em cm
AGE = 32  # Idade em anos

# Credenciais da API da Nutritionix, armazenadas em variáveis de ambiente para segurança
APP_ID = os.environ.get("ENV_NIX_APP_ID")
API_KEY = os.environ.get("ENV_NIX_API_KEY")

# Verifica se as credenciais estão definidas
if not APP_ID or not API_KEY:
    raise ValueError("As credenciais da Nutritionix não estão configuradas nas variáveis de ambiente.")

# URL do endpoint da API de exercícios naturais da Nutritionix
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Solicita ao usuário que digite os exercícios realizados
exercise_text = input("Quais exercícios você fez? ")

# Cabeçalhos da requisição contendo ID e chave da aplicação
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parâmetros enviados à API (com base nos dados do usuário e na descrição do exercício)
parameters = {
    "query": exercise_text,  # Texto descritivo dos exercícios
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Faz a requisição POST à API Nutritionix
response = requests.post(exercise_endpoint, json=parameters, headers=headers)

# Trata erros de resposta da API
try:
    response.raise_for_status()  # Lança exceção se status HTTP for erro
    result = response.json()  # Converte resposta JSON em dicionário Python
    print(f"Resposta da API Nutritionix:\n{result}\n")
except requests.exceptions.RequestException as e:
    print("Erro ao consultar a API Nutritionix:", e)
    exit()

# Captura a data e hora atuais formatadas
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

# Nome da aba da planilha no Google Sheets
GOOGLE_SHEET_NAME = "workout"

# Endpoint da API Sheety, também protegido via variável de ambiente
sheet_endpoint = os.environ.get("ENV_SHEETY_ENDPOINT")
if not sheet_endpoint:
    raise ValueError("O endpoint da API Sheety não está definido nas variáveis de ambiente.")

# Envia cada exercício extraído para a planilha via API Sheety
for exercise in result["exercises"]:
    # Monta o corpo da requisição com os dados do exercício
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),  # Nome capitalizado
            "duration": exercise["duration_min"],  # Duração em minutos
            "calories": exercise["nf_calories"]  # Calorias queimadas
        }
    }

    # Autenticação com usuário e senha (Basic Auth)
    SHEETY_USER = os.environ.get("ENV_SHEETY_USERNAME")
    SHEETY_PASS = os.environ.get("ENV_SHEETY_PASSWORD")
    if not SHEETY_USER or not SHEETY_PASS:
        raise ValueError("Usuário e/ou senha da API Sheety não estão definidos.")

    # Faz a requisição POST para Sheety com autenticação básica
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(SHEETY_USER, SHEETY_PASS)
    )

    # Verifica o sucesso da operação
    if sheet_response.status_code == 200 or sheet_response.status_code == 201:
        print("Dados enviados com sucesso para o Google Sheets.")
    else:
        print(f"Erro ao enviar dados para o Sheety:\n{sheet_response.text}")
