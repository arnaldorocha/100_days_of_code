# Note, Instagram will update it's website. So the CSS Selectors and XPATH may change.


import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
SIMILAR_ACCOUNT = "buzzfeedtasty"  # Pode trocar pelo nome de qualquer conta pública

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # Mantém navegador aberto após execução

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                       options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        wait = WebDriverWait(self.driver, 15)

        # Aguarda os campos de login aparecerem
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")

        # Preenche login
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        # Aguarda carregamento e ignora pop-ups
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Agora não')]"))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Agora não')]"))).click()
        except:
            pass  # Se os botões não aparecerem, continua

    def find_followers(self):
        # Vai até a página de seguidores da conta desejada
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5)

        # Espera o modal carregar
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@class='_aano']"))
        )

        # Rola o modal para carregar mais seguidores
        for _ in range(5):  # Ajuste o número de rolagens conforme quiser
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Procura os botões "Seguir"
        buttons = self.driver.find_elements(By.XPATH, "//button[normalize-space()='Seguir']")

        for button in buttons:
            try:
                button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                try:
                    # Fecha diálogo de confirmação se já segue
                    cancel_btn = self.driver.find_element(By.XPATH, "//button[text()='Cancelar']")
                    cancel_btn.click()
                except NoSuchElementException:
                    pass


if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
