from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
CSV_FILE = 'tasks.csv'

def read_tasks():
    tasks = []
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'title', 'due_date', 'completed'])
        return tasks

    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['completed'] = True if row['completed'] == 'True' else False
            tasks.append(row)
    return tasks

def save_tasks(tasks):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'title', 'due_date', 'completed']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)

@app.route('/')
def index():
    tasks = read_tasks()
    tasks.sort(key=lambda x: x['due_date'])
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    due_date = request.form.get('due_date')
    if title and due_date:
        tasks = read_tasks()
        new_id = str(int(tasks[-1]['id']) + 1) if tasks else '1'
        tasks.append({'id': new_id, 'title': title, 'due_date': due_date, 'completed': False})
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == id:
            task['completed'] = not task['completed']
            break
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task['id'] != id]
    save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
