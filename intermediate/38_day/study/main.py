# Importa bibliotecas
import requests  # Usada para realizar requisições HTTP (POST, PUT, DELETE)
from datetime import datetime  # Para capturar a data atual
import os  # Usado para acessar variáveis de ambiente com segurança

# ====== CONFIGURAÇÕES DO USUÁRIO ======
# As credenciais do Pixela devem ser definidas em variáveis de ambiente
USERNAME = os.environ.get("ENV_PIXELA_USERNAME")
TOKEN = os.environ.get("ENV_PIXELA_TOKEN")
GRAPH_ID = os.environ.get("ENV_PIXELA_GRAPH_ID")

# Verifica se os dados sensíveis estão configurados corretamente
if not USERNAME or not TOKEN or not GRAPH_ID:
    raise ValueError("Credenciais do Pixela ausentes. Configure as variáveis de ambiente.")

# Endpoint base da API Pixela
pixela_endpoint = "https://pixe.la/v1/users"

# ====== CRIAÇÃO DE USUÁRIO ======
# Parâmetros para criar um novo usuário Pixela (somente se for o primeiro uso)
user_params = {
    "token": TOKEN,  # Token secreto gerado pelo usuário
    "username": USERNAME,
    "agreeTermsOfService": "yes",  # Necessário para aceitar os termos da API
    "notMinor": "yes",  # Declaração de maioridade (obrigatório)
}

# Para criar o usuário, descomente abaixo:
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ====== CRIAÇÃO DE UM GRÁFICO ======
# Endpoint para criar o gráfico
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Configuração do gráfico (nome, unidade de medida, tipo e cor)
graph_config = {
    "id": GRAPH_ID,  # Identificador único do gráfico (sem espaços ou caracteres especiais)
    "name": "Cycling Graph",  # Nome exibido no painel do Pixela
    "unit": "Km",  # Unidade de medida (pode ser "Km", "minutes", etc.)
    "type": "float",  # Tipo de dado: "int" ou "float"
    "color": "ajisai"  # Cor do gráfico (azul-roxo). Outras opções: "shibafu", "momiji", "sora"
}

# Cabeçalho necessário para autenticação (envia o token do usuário)
headers = {
    "X-USER-TOKEN": TOKEN
}

# Para criar o gráfico, descomente abaixo:
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ====== CRIAÇÃO DE UM PONTO (pixel) ======
# Endpoint para adicionar um novo pixel no gráfico
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Captura a data atual no formato exigido pelo Pixela: AAAAMMDD
today = datetime.now().strftime("%Y%m%d")

# Dados do pixel, com entrada de quantidade feita pelo usuário
pixel_data = {
    "date": today,  # Data no formato exigido
    "quantity": input("Quantos quilômetros você pedalou hoje? ")  # Entrada do usuário
}

# Envia o pixel (ponto) para o gráfico
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# Mostra a resposta da API
print("Resposta ao adicionar pixel:", response.text)

# ====== ATUALIZAÇÃO DE UM PONTO EXISTENTE ======
# Endpoint específico para o pixel do dia atual
update_endpoint = f"{pixel_creation_endpoint}/{today}"

# Novo valor de quantidade para atualizar
new_pixel_data = {
    "quantity": "4.5"  # Novo valor a ser registrado
}

# Para atualizar um pixel, descomente abaixo:
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print("Resposta ao atualizar pixel:", response.text)

# ====== REMOÇÃO DE UM PONTO EXISTENTE ======
delete_endpoint = f"{pixel_creation_endpoint}/{today}"

# Para deletar o pixel do dia, descomente abaixo:
# response = requests.delete(url=delete_endpoint, headers=headers)
# print("Resposta ao deletar pixel:", response.text)
