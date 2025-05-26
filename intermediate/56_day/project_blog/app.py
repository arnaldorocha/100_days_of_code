from flask import Flask, render_template, request, redirect, url_for, flash
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Dados dos posts de exemplo (você pode substituir por API ou banco de dados)
posts = [
    {
        "id": 1,
        "title": "Meu primeiro projeto",
        "subtitle": "Iniciando com Python",
        "author": "Arnaldo Rocha",
        "date": "2025-01-01",
        "content": "Este é o conteúdo do meu primeiro post."
    },
    {
        "id": 2,
        "title": "Segundo Projeto",
        "subtitle": "Explorando Flask",
        "author": "Arnaldo Rocha",
        "date": "2025-02-10",
        "content": "Mais um projeto utilizando Flask e Jinja."
    }
]

# Criação do app Flask
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Necessário para usar flash()

# ROTAS
@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        if name and email and message:
            success = send_email(name, email, phone, message)
            if success:
                flash("Mensagem enviada com sucesso!", "success")
            else:
                flash("Erro ao enviar a mensagem. Tente novamente mais tarde.", "danger")
        else:
            flash("Preencha todos os campos obrigatórios.", "warning")
        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = next((post for post in posts if post["id"] == index), None)
    if requested_post:
        return render_template("post.html", post=requested_post)
    return "<h1>Post não encontrado</h1>", 404

# FUNÇÃO DE ENVIO DE EMAIL

def send_email(name, email, phone, message):
    email_msg = EmailMessage()
    email_msg["Subject"] = "Novo Contato do Portfólio"
    email_msg["From"] = os.getenv("MY_EMAIL")
    email_msg["To"] = os.getenv("MY_EMAIL")

    email_msg.set_content(
        f"Nome: {name}\nEmail: {email}\nTelefone: {phone}\n\nMensagem:\n{message}",
        charset="utf-8"
    )

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
            connection.send_message(email_msg)
            print("✅ Email enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")
        
# EXECUÇÃO DO SERVIDOR
if __name__ == "__main__":
    app.run(debug=True, port=5001)
