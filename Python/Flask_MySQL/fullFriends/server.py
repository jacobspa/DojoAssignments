from flask import Flask, redirect, request, session, flash, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'Full Friends')
app.secret_key = 'thisIsSecret'

@app.route('/')
def home():
    all_friends = mysql.query_db('select * from friends')
    return render_template('index.html', friends=all_friends)

@app.route('/friends', methods=['POST'])
def addFriend():
    first = request.form['html_first']
    last = request.form['html_last']
    email = request.form['html_email']
    parameters = {
                'first_name': first,
                'last_name': last,
                'email': email,
    }
    query = 'INSERT INTO friends(first_name, last_name, email, created_at) VALUES(:first_name, :last_name, :email, NOW())'
    mysql.query_db(query, parameters)
    return redirect('/')

@app.route('/friends/<ident>/edit', methods=['POST'])
def editFriend(ident):
    session['id'] = ident
    return render_template('editFriend.html', id=session['id'])

@app.route('/friends/<ident>', methods=['POST'])
def handleEdit(ident):
    first = request.form['html_first']
    last = request.form['html_last']
    email = request.form['html_email']
    parameters = {
                'first_name': first,
                'last_name': last,
                'email': email,
                'id': session['id']
    }
    query = 'UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id'
    mysql.query_db(query, parameters)
    return redirect('/')

@app.route('/friends/<ident>/delete', methods=['POST'])
def deleteFriend(ident):
    parameters ={
                'id': ident
    }
    query = 'DELETE from friends WHERE id=:id'
    mysql.query_db(query, parameters)
    return redirect('/')

app.run(debug=True)
