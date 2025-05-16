
# Automação de candidaturas no LinkedIn com Selenium
# ⚠️ Este script é para fins educacionais. Automatizar ações em sites como o LinkedIn pode violar seus termos de uso.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Substitua com suas informações ou use variáveis de ambiente seguras
ACCOUNT_EMAIL = "YOUR_LOGIN_EMAIL"
ACCOUNT_PASSWORD = "YOUR_LOGIN_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"

# Função para cancelar candidatura complexa (mais de 1 etapa)
def abort_application():
    # Fecha a janela/modal de candidatura
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()
    time.sleep(2)
    # Confirma o descarte da candidatura
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Caminho do ChromeDriver (manual)
chrome_driver_path = "YOUR_CHROME_DRIVER_PATH"

# Alternativa automática com webdriver-manager (recomendado)
from webdriver_manager.chrome import ChromeDriverManager
chrome_driver_path = ChromeDriverManager(path="YOUR_CHROME_DRIVER_FOLDER").install()

# Mantém o navegador aberto após o script (útil para testes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Inicia o navegador com o ChromeDriver
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre a página de buscas de vagas no LinkedIn
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Aguarda o carregamento e rejeita cookies (se botão existir)
time.sleep(2)
try:
    reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
    reject_button.click()
except NoSuchElementException:
    pass

# Clica em "Sign in" para logar
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Preenche email e senha
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Espera o usuário resolver o captcha manualmente
input("Pressione ENTER após resolver o CAPTCHA...")

# Coleta todas as listagens de vagas na página
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Itera sobre todas as vagas
for listing in all_listings:
    print("Abrindo vaga...")
    listing.click()
    time.sleep(2)
    try:
        # Tenta encontrar e clicar no botão de aplicar
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Aguarda o modal abrir e preenche o telefone se necessário
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Verifica se a candidatura é simples ou complexa
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Candidatura complexa. Ignorada.")
            continue
        else:
            # Candidatura simples: envia
            print("Enviando candidatura...")
            submit_button.click()

        # Fecha a janela após aplicar
        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        # Caso não haja botão de aplicar ou outro erro
        abort_application()
        print("Sem botão de aplicar. Ignorada.")
        continue

# Encerra o navegador após as candidaturas
time.sleep(5)
driver.quit()
