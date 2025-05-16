from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ===================== CONFIGURAÇÕES =====================
# Termo a ser pesquisado no LinkedIn
SEARCH_QUERY = "people who study Python"

# Mensagem personalizada para o convite
MESSAGE = "Olá! Vi que você estuda Python, vamos nos conectar 🙂"

# Número máximo de convites a serem enviados
MAX_INVITES = 10

# ===================== SETUP DO DRIVER =====================
# Define opções do Chrome para manter o navegador aberto após execução
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Instala e configura o ChromeDriver automaticamente
service = Service(ChromeDriverManager().install())

# Cria o driver com as opções definidas
driver = webdriver.Chrome(service=service, options=options)

# ===================== ACESSO AO LINKEDIN =====================
# Abre a página inicial do LinkedIn
driver.get("https://www.linkedin.com/")

# Aguarda o login manual (recomendado por causa de CAPTCHA e 2FA)
input("\n➡️ Faça login no LinkedIn manualmente e pressione Enter aqui para continuar...\n")

# ===================== PESQUISA POR PERFIS =====================
# Localiza a barra de pesquisa e envia a consulta definida em SEARCH_QUERY
search_bar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
search_bar.send_keys(SEARCH_QUERY)
search_bar.send_keys(Keys.RETURN)

# Aguarda os resultados carregarem
time.sleep(3)

# Clica na aba "Pessoas" para filtrar os resultados
people_button = driver.find_element(By.LINK_TEXT, "People")
people_button.click()

# Aguarda o carregamento da nova página
time.sleep(3)

# ===================== ENVIO DE CONVITES =====================
sent = 0  # Contador de convites enviados

# Coleta os resultados da pesquisa (perfis visíveis na tela)
profiles = driver.find_elements(By.CSS_SELECTOR, ".reusable-search__result-container")

# Itera pelos perfis encontrados
for profile in profiles:
    if sent >= MAX_INVITES:
        break  # Para se atingir o limite definido

    try:
        # Tenta encontrar o botão "Conectar" no resultado atual
        connect_button = profile.find_element(By.TAG_NAME, "button")
        if connect_button.text.strip().lower() == "connect":
            # Rola até o botão (caso esteja fora da tela)
            driver.execute_script("arguments[0].scrollIntoView();", connect_button)
            connect_button.click()
            time.sleep(2)

            # Clica em "Adicionar uma nota" para incluir mensagem personalizada
            add_note = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
            add_note.click()
            time.sleep(1)

            # Insere a mensagem no campo de texto
            message_box = driver.find_element(By.ID, "custom-message")
            message_box.send_keys(MESSAGE)

            # Clica no botão "Enviar agora"
            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
            send_button.click()

            # Atualiza o contador e imprime status
            sent += 1
            print(f"✅ Convite enviado ({sent}/{MAX_INVITES})")
            time.sleep(2)
        else:
            print("🔁 Não é um perfil conectável ou já está conectado.")

    except Exception as e:
        print("⚠️ Erro ao tentar enviar convite:", e)
        continue

# Fim do script
print("\n🚀 Todos os convites enviados ou limite alcançado. Script finalizado.")
