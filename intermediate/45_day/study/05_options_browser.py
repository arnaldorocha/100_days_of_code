# Mantém o navegador aberto após execução (útil para testes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Inicia o navegador com o ChromeDriver configurado
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
