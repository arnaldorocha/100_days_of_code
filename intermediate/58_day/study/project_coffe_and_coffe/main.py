from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os

# Caminho absoluto do CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "cafes.csv")

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'),
)

app.config['SECRET_KEY'] = 'segredo_seguro_aqui'
Bootstrap5(app)

class CafeForm(FlaskForm):
    nome = StringField('Nome do Café', validators=[DataRequired()])
    localizacao = StringField("Link do Google Maps", validators=[DataRequired(), URL()])
    abertura = StringField("Horário de Abertura (ex: 08:00)", validators=[DataRequired()])
    fechamento = StringField("Horário de Fechamento (ex: 18:00)", validators=[DataRequired()])
    avaliacao_cafe = SelectField("Nota do Café", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    avaliacao_wifi = SelectField("Força do Wifi", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    avaliacao_energia = SelectField("Tomadas Disponíveis", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    enviar = SubmitField('Adicionar')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/adicionar', methods=["GET", "POST"])
def adicionar():
    form = CafeForm()
    if form.validate_on_submit():
        with open(CSV_PATH, mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.nome.data},"
                           f"{form.localizacao.data},"
                           f"{form.abertura.data},"
                           f"{form.fechamento.data},"
                           f"{form.avaliacao_cafe.data},"
                           f"{form.avaliacao_wifi.data},"
                           f"{form.avaliacao_energia.data}")
        return redirect(url_for('cafes'))
    return render_template('adicionar.html', form=form)

@app.route('/cafes')
def cafes():
    with open(CSV_PATH, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        lista_cafes = list(csv_data)
    return render_template('cafes.html', cafes=lista_cafes)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
