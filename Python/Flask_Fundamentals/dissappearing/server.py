from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'This is the secret_key'

@app.route('/')
def noNinjas():
    return render_template('index.html')

@app.route('/ninja')
def allOfThem():
    return render_template('turtle.html', turtle="turtle")



@app.route('/ninja/<color>')
def display(color):
    if color == 'blue':
        turtle = 'leonardo'
    elif color == 'red':
        turtle = 'raphael'
    elif color == 'orange':
        turtle = 'michelangelo'
    elif color == 'purple':
        turtle = 'donatello'
    else:
        turtle = 'hacker!'
    return render_template('turtle.html', turtle=turtle)

app.run(debug=True)
