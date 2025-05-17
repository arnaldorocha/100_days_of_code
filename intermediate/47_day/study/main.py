from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# ✅ Valores prometidos pelo provedor
PROMISED_DOWN = 150  # Mbps
PROMISED_UP = 10     # Mbps

# 🔐 Pegando dados sensíveis do ambiente
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        # Inicializa o navegador Chrome com webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """Abre o Speedtest.net e mede a velocidade atual da internet."""
        print("🔄 Medindo velocidade da internet...")
        self.driver.get("https://www.speedtest.net/")

        # Espera botão "Go" carregar e clica
        go_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
        )
        go_button.click()

        # Aguarda o teste ser concluído (tempo pode variar)
        time.sleep(45)

        # Captura os valores de download e upload exibidos na página
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

        print(f"📉 Download: {self.down} Mbps")
        print(f"📈 Upload: {self.up} Mbps")

    def tweet_at_provider(self):
        """Faz login no Twitter e envia um tweet reclamando da velocidade."""
        print("🔐 Fazendo login no Twitter...")
        self.driver.get("https://twitter.com/login")

        # Espera até que os campos estejam visíveis
        email_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)

        time.sleep(2)

        # Pode ser necessário lidar com múltiplas etapas de login
        try:
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
        except:
            print("⚠️ Não foi possível completar o login.")

        time.sleep(5)

        print("✍️ Escrevendo tweet...")
        tweet = (
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
            f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? #internetfail"
        )

        tweet_box = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[aria-label='Tweet text']")
            )
        )
        tweet_box.send_keys(tweet)

        # Clica no botão de tweetar
        tweet_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]'))
        )
        tweet_button.click()

        print("✅ Tweet enviado!")
        self.driver.quit()


# 🚀 Execução do bot
if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
