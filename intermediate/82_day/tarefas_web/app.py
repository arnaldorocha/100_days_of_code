from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
CSV_FILE = 'tarefas.csv'

def ler_tarefas():
    tarefas = []
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'descricao', 'concluida', 'data_hora'])
        return tarefas

    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['concluida'] = True if row['concluida'] == 'True' else False
            tarefas.append(row)
    return tarefas

def salvar_tarefas(tarefas):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'descricao', 'concluida', 'data_hora']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tarefa in tarefas:
            writer.writerow(tarefa)

@app.route('/')
def index():
    tarefas = ler_tarefas()
    # ordenar por data_hora (pode converter string para facilitar)
    tarefas.sort(key=lambda x: x['data_hora'])
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao')
    data_hora = request.form.get('data_hora')
    if descricao and data_hora:
        tarefas = ler_tarefas()
        novo_id = str(int(tarefas[-1]['id']) + 1) if tarefas else '1'
        tarefas.append({'id': novo_id, 'descricao': descricao, 'concluida': False, 'data_hora': data_hora})
        salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/concluir/<id>')
def concluir(id):
    tarefas = ler_tarefas()
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['concluida'] = not tarefa['concluida']
            break
    salvar_tarefas(tarefas)
    return redirect(url_for('index'))

@app.route('/deletar/<id>')
def deletar(id):
    tarefas = ler_tarefas()
    tarefas = [t for t in tarefas if t['id'] != id]
    salvar_tarefas(tarefas)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
