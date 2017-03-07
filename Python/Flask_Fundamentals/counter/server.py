from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def counter():
    session['amount']= session['amount'] + 1
    return render_template('index.html', counter=session['amount'])

@app.route('/ninjas')
def increment_two():
    session['amount'] = session['amount'] + 1
    return redirect('/')

@app.route("/hackers")
def reset_count():
    session['amount'] = -1
    return redirect('/')
app.run(debug=True)
