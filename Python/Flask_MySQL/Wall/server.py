from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re, datetime

app = Flask(__name__)
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'Wall')
app.secret_key = 'thisIsSecret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['html_email']

    password = request.form['html_pass']
    is_valid = True
    details = {
            'email': email
    }

    print "========="
    print email
    print "========="

    query = 'SELECT * FROM users WHERE email = :email'
    user = mysql.query_db(query, details)
    if len(user) > 0:
        if email_regex.search(email) is None:
            flash('Email is not valid!')
            is_valid = False
        elif password != user[0]['password']:
            flash('Invalid password!')
            is_valid = False
        if is_valid:
            setup_session(user, email)
            return redirect('/wall')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    first = request.form['html_first']
    last = request.form['html_last']
    email = request.form['html_email']
    password = request.form['html_pass']
    confirm = request.form['html_confirm']
    is_valid = True

    if len(first) < 2:
        flash('First Name must be greater than 2 characters!')
        is_valid = False
    if len(last) < 2:
        flash('Last Name must be greater than 2 character!')
        is_valid = False
    if email_regex.search(email) is None:
        flash('Email is not Valid!')
        is_valid = False
    if len(password) < 1:
        flash('Password field must be filled out!')
        is_valid = False
    if len(confirm) < 1:
        flash('Must Confirm password!')
        is_valid = False
    if password != confirm:
        flash('Passwords do not match!')
        is_valid = False
    if is_valid:
        flash('Successfully Registered!')
        parameters = {
                    'first_name': first,
                    'last_name': last,
                    'email': email,
                    'password': password,
        }
        query = 'INSERT INTO users(first_name, last_name, email, password, created_at) VALUES(:first_name, :last_name, :email, :password, NOW())'
        user_id = mysql.query_db(query, parameters)
        setup_session(user_id, email)
        return redirect('/wall')
    return redirect('/')

@app.route('/wall')
def wall():
    return render_template('wall.html')

@app.route('/process', methods=['POST'])
def process():
    message = request.form['message']
    query_message = 'SELECT * from messages'
    db_messages = mysql.query_db(query_message)
    parameters = {
                'message': message,
                'created_at': datetime.datetime.now()
                'user_id': session['id']
    }
    query = 'INSERT INTO messages(message, user_id created_at) VALUES(:message, :user_id, :created_at)'
    user_id = mysql.query_db(query,parameters)
    setup_session(user_id, email)
    print '______________________'
    print user_id
    print '_______________________'

    return redirect('/wall')

def setup_session(user_id, email):
    session['id'] = user_id
    session['email'] = email

app.run(debug=True)
