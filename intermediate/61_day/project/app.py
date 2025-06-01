from flask import Flask, render_template, request, redirect, send_file
from datetime import datetime
import csv
import random
from collections import defaultdict
import io
import os

app = Flask(__name__)

DATA_FILE = 'data.csv'
MOTIVATIONAL_MESSAGES = [
    "Você está indo muito bem!",
    "Um dia de cada vez. Você consegue!",
    "Valorize cada pequeno progresso.",
    "Seu bem-estar importa!",
    "Persistência é a chave do sucesso."
]


def load_entries():
    entries = []

    # Cria o arquivo se não existir
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'mood', 'note'])

    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
            row['mood'] = int(row['mood'])
            entries.append(row)
    return entries

def get_weekly_average(entries):
    weekly = defaultdict(list)
    for entry in entries:
        year_week = entry['date'].strftime('%Y-%U')
        weekly[year_week].append(entry['mood'])
    return {k: sum(v)/len(v) for k, v in weekly.items()}

def get_monthly_average(entries):
    monthly = defaultdict(list)
    for entry in entries:
        year_month = entry['date'].strftime('%Y-%m')
        monthly[year_month].append(entry['mood'])
    return {k: sum(v)/len(v) for k, v in monthly.items()}

@app.template_filter('format_date')
def format_date(value, format='%d/%m'):
    return value.strftime(format)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        mood = request.form['mood']
        note = request.form['note']
        with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date, mood, note])
        return redirect('/')

    entries = load_entries()
    entries.sort(key=lambda x: x['date'])

    # Filtro por data
    start_date = request.args.get('start')
    end_date = request.args.get('end')
    if start_date and end_date:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        entries = [e for e in entries if start <= e['date'] <= end]

    weekly_avg = get_weekly_average(entries)
    monthly_avg = get_monthly_average(entries)
    message = random.choice(MOTIVATIONAL_MESSAGES)

    return render_template('index.html', entries=entries, weekly=weekly_avg, monthly=monthly_avg, message=message)

@app.route('/export')
def export_data():
    entries = load_entries()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['date', 'mood', 'note'])
    for entry in entries:
        writer.writerow([entry['date'].strftime('%Y-%m-%d'), entry['mood'], entry['note']])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', download_name='mood_data.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
