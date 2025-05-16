# Caso não haja botão de aplicar pra vaga

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

# Finaliza após aplicar em todas as vagas

time.sleep(5)
driver.quit()
