from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- CONFIGURAÇÕES ---
SEARCH_QUERY = "people who study Python"
MESSAGE = "Olá! Vi que você estuda Python, vamos nos conectar 🙂"
MAX_INVITES = 10  # número máximo de convites a enviar

# --- SETUP DO DRIVER ---
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Mantém o navegador aberto após execução

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- ACESSA O LINKEDIN ---
driver.get("https://www.linkedin.com/")
input("Faça login no LinkedIn manualmente e pressione Enter aqui para continuar...")

# --- PESQUISA POR PESSOAS COM PYTHON NO PERFIL ---
search_bar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
search_bar.send_keys(SEARCH_QUERY)
search_bar.send_keys(Keys.RETURN)

time.sleep(3)

# Filtra apenas por pessoas
people_button = driver.find_element(By.LINK_TEXT, "People")
people_button.click()
time.sleep(3)

# --- ENVIA CONVITES ---
sent = 0
profiles = driver.find_elements(By.CSS_SELECTOR, ".reusable-search__result-container")  # Resultados

for profile in profiles:
    if sent >= MAX_INVITES:
        break

    try:
        # Tenta encontrar o botão "Connect"
        connect_button = profile.find_element(By.TAG_NAME, "button")
        if connect_button.text.strip().lower() == "connect":
            driver.execute_script("arguments[0].scrollIntoView();", connect_button)
            connect_button.click()
            time.sleep(2)

            # Adiciona uma mensagem personalizada
            add_note = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
            add_note.click()
            time.sleep(1)

            message_box = driver.find_element(By.ID, "custom-message")
            message_box.send_keys(MESSAGE)

            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
            send_button.click()

            sent += 1
            print(f"Convite enviado ({sent}/{MAX_INVITES})")

            time.sleep(2)
        else:
            print("Não é um perfil conectável ou já conectado.")
    except Exception as e:
        print("Erro ao tentar enviar convite:", e)
        continue

print("Script finalizado.")
