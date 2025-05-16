
#função para cancelar candidaturas dificeis
def abort_application():
    # Fecha a janela modal (popup) da candidatura
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)

    # Confirma o descarte da candidatura
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()
