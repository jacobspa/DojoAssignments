from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def ninjaGold():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = ''
    return render_template('ninjaGold.html')

@app.route('/process_gold', methods=['POST'])
def proccess():
    if request.form['building'] == "farm":
        farmGold = random.randrange(10,21)
        session['activities'] += "Earned "+  str(farmGold) + " from the farm!\n"
        session['gold'] += farmGold
    elif request.form['building'] == "cave":
        caveGold= random.randrange(5,10)
        session['activities'] += "Earned "+ str(caveGold) +" from the cave!\n"
        session['gold'] += caveGold
    elif request.form['building'] == "house":
        houseGold = random.randrange(2,5)
        session['activities'] += "Earned "+ str(houseGold) +" from the house!\n"
        session['gold'] += houseGold
    elif request.form['building'] == 'casino':
        luck = random.randrange(0,2)
        if luck == 1:
            casinoGold= random.randrange(0,51)
            session['activities'] += "Earned "+ str(casinoGold) + " from the casino!\n"
            session['gold'] += casinoGold
        elif luck == 0:
            casinoGold = random.randrange(0,51)
            session['activities'] += "Lost "+ str(casinoGold) + " from the casino...\n"
            session['gold'] -= casinoGold
    return redirect('/')

app.run(debug=True)
