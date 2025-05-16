# 🤖 **LinkedIn Python Auto-Connector Bot**

Este projeto é um bot automatizado em Python que utiliza Selenium para enviar convites de conexão no LinkedIn apenas para pessoas que estudam ou trabalham com Python. Ideal para networking estratégico!

---

## 📌 **Pré-requisitos**

Antes de rodar este script, certifique-se de ter instalado:

Python 3.7+

Google Chrome

Pacotes Python:

pip install selenium webdriver-manager

🧠 Como o bot funciona — passo a passo


---

## 1. ⚙️ Configuração inicial

Você define:

A pesquisa no LinkedIn (people who study Python por padrão)

A mensagem de convite

A quantidade máxima de convites a enviar

## 2. 🧭 Acesso e login manual

O script abre o LinkedIn no navegador. Você faz o login manualmente e pressiona Enter no terminal para continuar (essa etapa evita bloqueios por captcha).

---

## 3. 🔍 Busca por perfis

Ele digita o termo de busca na barra do LinkedIn, pressiona Enter e filtra para mostrar apenas pessoas.

---

## 4. 📨 Envio de convites

Para cada resultado da pesquisa:

Verifica se há botão de "Conectar"

Clica em "Adicionar uma nota"

Insere uma mensagem personalizada

Envia o convite

---

## 5. 🛑 Parada automática

O script para de rodar ao atingir o número máximo de convites ou ao finalizar a lista de perfis visíveis.

---

### 📄 Exemplo de mensagem personalizada

Olá! Vi que você estuda Python, vamos nos conectar 🙂

Você pode personalizar a mensagem diretamente na variável MESSAGE no início do código.

### ⚠️ **Avisos importantes**

Respeite os termos de uso do LinkedIn — use com moderação.

O LinkedIn pode limitar o número de convites diários.

Perfis com "Conectar" indisponível serão pulados automaticamente.

O script interage apenas com perfis visíveis na página atual.

### ✅ Benefícios de usar este bot

Praticar automação com Selenium

Aprender como interagir com páginas web dinamicamente

Facilitar networking segmentado e inteligente

### 🚀 Comece agora

Clone ou copie este repositório

Edite os campos SEARCH_QUERY, MESSAGE e MAX_INVITES se quiser

Execute o script com:

python linkedin_bot.py

Faça login no LinkedIn e pressione Enter

Observe o bot conectar com a comunidade Python!

Feito com 💻 por entusiastas de automação e Python.

📬 Sugestões e melhorias são bem-vindas!
