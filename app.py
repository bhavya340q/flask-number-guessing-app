from flask import Flask,render_template,redirect,request,session,url_for
from random import randint

app = Flask(__name__)
app.secret_key = "BvuL]2+H/^<aq<n"

@app.route("/", methods=["POST", "GET"])
def home():
    if 'number' not in session:
        session['number'] = randint(1, 100)
        session['tries'] = 0

    if request.method == "POST":
        guess = int(request.form['guess'])
        num = session['number']
        session['tries'] += 1

        if guess > num:
            return render_template("index.html", message='Guess is Higher')
        elif guess < num:
            return render_template("index.html", message='Guess is Smaller')
        else:
            message = f'You guessed it correctly in {session["tries"]} tries!'
            session.pop('number')
            session.pop('tries')
            return render_template("index.html", message=message)

    return render_template("index.html")

@app.route("/reset",methods=["GET"])
def reset():
    session.pop('number')
    session.pop('tries')
    return redirect(url_for('home'))
