# Início do processo de candidatura


    try:
        # Tenta encontrar e clicar no botão de aplicar
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)

        # Localiza campo de telefone e preenche se estiver vazio
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)
