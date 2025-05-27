🔹 Importações e Comentários Iniciais
python
Copiar
Editar
from flask import Flask, render_template 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
✅ Explicação:
Flask: framework para criar aplicações web.

render_template: função do Flask para renderizar arquivos HTML.

FlaskForm: classe base para criar formulários com a extensão Flask-WTF.

StringField, PasswordField, SubmitField: tipos de campos de formulário (texto, senha, botão).

validators: funções que garantem que os dados inseridos estão corretos (ex: não vazios, formato de e-mail etc).

Bootstrap5: integração com o framework CSS Bootstrap para deixar o site mais bonito.

🔹 Comentário sobre instalação de pacotes

'''
Red underlines? Install the required packages first: 
...
'''
Esse bloco de comentário é um aviso: se o código estiver sublinhado em vermelho (erros), provavelmente os pacotes necessários não estão instalados. Ele mostra como instalar os pacotes com pip.

🔹 Definindo o formulário de login

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

✅ Explicação:
Aqui criamos uma classe de formulário chamada LoginForm.

email: campo de texto que deve ser preenchido (DataRequired()).

password: campo de senha também obrigatório.

submit: botão com o rótulo "Log In".

🔹 Configuração do app Flask

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

✅ Explicação:
Criamos o app com Flask(__name__).

secret_key: usada pelo Flask-WTF para proteger o formulário contra ataques CSRF.

Bootstrap5(app): aplica os estilos do Bootstrap automaticamente aos formulários.

🔹 Rota da página inicial

@app.route("/")
def home():
    return render_template('index.html')

✅ Explicação:
Quando o usuário acessa / (página inicial), o Flask renderiza o arquivo index.html.

🔹 Rota da página de login

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

✅ Explicação:
@app.route("/login", methods=["GET", "POST"]): essa rota aceita tanto o carregamento da página (GET) quanto o envio do formulário (POST).

login_form = LoginForm(): cria um objeto do formulário.

validate_on_submit(): verifica se o formulário foi enviado (POST) e se os campos são válidos.

Verificamos se os dados são os esperados:

Se corretos → mostra success.html.

Se incorretos → mostra denied.html.

Se o formulário ainda não foi enviado, exibe login.html com o formulário.

🔹 Executando o servidor Flask

if __name__ == '__main__':
    app.run(debug=True, port=5001)

✅ Explicação:
Garante que o código só será executado se rodarmos diretamente este arquivo.

debug=True: ativa o modo de depuração (ajuda durante o desenvolvimento).

port=5001: o servidor rodará em http://localhost:5001.

📝 Resumo Visual do Fluxo:
/ (index.html) — Página inicial simples.

/login (login.html) — Mostra o formulário.

submit — Se dados corretos → success.html. Se errados → denied.html.