
# Verifica se é uma candidatura simples ou complexa

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")

        # Se for uma candidatura com várias etapas, cancela
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Candidatura simples: envia!
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)

        # Fecha o modal após se candidatar
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()





