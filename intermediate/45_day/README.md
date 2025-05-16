# 🤖 Bot de Candidatura Automática no LinkedIn com Selenium

Este projeto automatiza o processo de candidatura a vagas no LinkedIn usando a biblioteca Selenium com Python. Ele percorre os anúncios de emprego e se candidata automaticamente àqueles com processo simples ("Easy Apply").

---

## 📌 Requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.x
- Google Chrome
- ChromeDriver compatível com sua versão do navegador
- Bibliotecas Python:
  ```bash
  pip install selenium webdriver-manager
  ```

---

## ⚙️ Configuração

No código, substitua os seguintes valores:

```python
ACCOUNT_EMAIL = "SEU EMAIL"
ACCOUNT_PASSWORD = "SUA SENHA"
PHONE = "SEU TELEFONE"
```

O ChromeDriver será instalado automaticamente com o `webdriver-manager`, então você não precisa baixar manualmente.

---

## 🧠 Como o Bot Funciona — Passo a Passo

### 1. Inicialização do Navegador

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
```
Mantém o navegador aberto após a execução (útil para debug).

### 2. Acesso à Página de Vagas no LinkedIn

```python
driver.get("https://www.linkedin.com/jobs/search/...")
```
Abre a página de resultados para uma busca de vagas com filtros pré-definidos (como localização e palavra-chave).

### 3. Aceite ou Rejeição de Cookies

```python
reject_button = driver.find_element(...)
reject_button.click()
```
Fecha o pop-up de cookies se estiver presente.

### 4. Login no LinkedIn

```python
sign_in_button = driver.find_element(...)
sign_in_button.click()

email_field = driver.find_element(...)
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(...)
password_field.send_keys(ACCOUNT_PASSWORD)
```
Faz login na conta LinkedIn.

⚠️ **IMPORTANTE**: Após o login, o LinkedIn pode pedir um CAPTCHA. Resolva manualmente antes de continuar.

---

### 5. Captura dos Anúncios

```python
all_listings = driver.find_elements(...)
```
Coleta todas as vagas exibidas na página.

### 6. Loop de Aplicação

```python
for listing in all_listings:
    listing.click()
    apply_button = driver.find_element(...)
```
Clica em cada vaga e tenta aplicar.

### 7. Preenchimento de Dados

```python
phone = driver.find_element(...)
phone.send_keys(PHONE)
```
Insere o número de telefone, se o campo estiver vazio.

### 8. Validação do Tipo de Aplicação

```python
if submit_button.get_attribute("data-control-name") == "continue_unify":
    abort_application()
```
Ignora candidaturas que exigem múltiplas etapas (currículo, perguntas adicionais, etc).

### 9. Submissão

```python
submit_button.click()
```
Finaliza a candidatura e fecha a janela de confirmação.

---

## 🛑 Finalização

```python
driver.quit()
```
Fecha o navegador após o loop.

---

## 📌 Observações

- O bot só aplica para vagas com o botão **"Easy Apply"**.
- Funciona melhor com filtros bem definidos no link de busca.
- Não se responsabiliza por uso indevido. Automação em sites de terceiros deve seguir os termos de uso.

---

## ✅ Conclusão

Este projeto é uma ótima introdução a:

- Automação com Selenium
- Interação com elementos web
- Controle de fluxo e tratamento de exceções