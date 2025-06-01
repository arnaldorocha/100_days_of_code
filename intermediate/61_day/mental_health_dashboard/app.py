from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mood.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    mood = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(200))

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    entries = MoodEntry.query.order_by(MoodEntry.date.desc()).all()
    labels = [entry.date.strftime('%d/%m') for entry in entries]
    moods = [entry.mood for entry in entries]
    return render_template('index.html', entries=entries, labels=labels, moods=moods)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        mood = request.form['mood']
        note = request.form['note']
        new_entry = MoodEntry(mood=mood, note=note)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
