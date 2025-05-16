# Importa o módulo principal do Selenium para controlar o navegador
from selenium import webdriver

# Permite simular pressionamento de teclas como ENTER, TAB, etc.
from selenium.webdriver.common.keys import Keys

# Usado para tratar erros caso um elemento não seja encontrado na página
from selenium.common.exceptions import NoSuchElementException

# Permite configurar e controlar o ChromeDriver com mais flexibilidade
from selenium.webdriver.chrome.service import Service as ChromeService

# Utilizado para localizar elementos pelo ID, classe, seletor CSS, etc.
from selenium.webdriver.common.by import By

# Biblioteca padrão do Python para controlar o tempo (delays, contagem etc.)
import time
