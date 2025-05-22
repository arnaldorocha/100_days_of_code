from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "segredo-super-seguro"  # Necessário para usar sessões


@app.route("/", methods=["GET", "POST"])
def home():
    if "number" not in session:
        session["number"] = random.randint(0, 9)

    if request.method == "POST":
        guess = int(request.form["guess"])
        number = session["number"]
        if guess > number:
            result = {"message": "Muito alto, tente de novo!", "color": "purple",
                      "gif": "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"}
        elif guess < number:
            result = {"message": "Muito baixo, tente de novo!", "color": "red",
                      "gif": "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"}
        else:
            result = {"message": "Você acertou!", "color": "green",
                      "gif": "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"}
            session.pop("number", None)  # Reinicia o jogo
        return render_template("result.html", result=result)

    return render_template("index.html")


@app.route("/restart")
def restart():
    session["number"] = random.randint(0, 9)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
