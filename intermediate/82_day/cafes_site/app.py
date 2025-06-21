from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

# Caminho absoluto para o arquivo cafes.csv dentro da pasta cafes_site
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'cafes.csv')

# Criar o arquivo CSV com cabeçalho se ainda não existir
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nome', 'Localização', 'WiFi', 'Tomada', 'Café'])

# Página inicial: Lista todos os cafés
@app.route('/')
def index():
    cafes = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Pula o cabeçalho
        for row in reader:
            cafes.append(row)
    return render_template('index.html', cafes=cafes)

# Página de adicionar novo café
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                request.form['name'],
                request.form['location'],
                request.form['wifi'],
                request.form['power'],
                request.form['coffee']
            ])
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
