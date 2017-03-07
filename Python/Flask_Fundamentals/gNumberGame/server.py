from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key ="ThisIsSecret"

@app.route('/')
def playGame():
    if 'number' not in session:
        session['number']= random.randrange(0,101)
    return render_template('game.html', number=session['number'])

@app.route('/process', methods=['POST'])
def process():
    session["userGuess"] = int(request.form['userGuess'])
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
