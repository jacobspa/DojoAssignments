from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'login')
app.secret_key = "thisIsSecret"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    password = request.form['html_pass']
    email = request.form['html_email']
    pw_input = bcrypt.generate_password_hash(password)
    print pw_input
    is_valid = True
    data = {
            'email': email
    }
    query = "SELECT * FROM users where email = :email"
    user = mysql.query_db(query, data)
    if  email_regex.search(email) is None:
        flash('email is not valid')
        is_valid = False
    if bcrypt.check_password_hash(user[0]['pw_hash'], pw_input) == False:
        flash('Incorrect password')
        is_valid = False
    print user[0]['pw_hash']
    if is_valid:
        setup_session(user, email)
        return redirect('/success')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    is_valid = True
    first = request.form['html_first']
    last = request.form['html_last']
    email = request.form['html_email']
    password = request.form['html_pass']
    if len(request.form['html_pass']) > 7:
        pw_hash = bcrypt.generate_password_hash(password)
    confirm = request.form['html_confirm']

    if len(first) < 2:
        flash('First Name must be longer than 2 characters!')
        is_valid = False
    if any(char.isdigit() for char in request.form['html_first']):
        flash('First name cannot contain any numbers')
        is_valid = False
    if any(char.isdigit() for char in request.form['html_last']):
        flash("Last name cannot contain any numbers")
        is_valid = False
    if len(last) < 2:
        flash('Last Name must be longer than 2 characters!')
        is_valid = False
    if email_regex.search(email) is None:
        flash('Email is not valid!')
        is_valid = False
    if len(password) < 8:
        flash('Password must be longer than 8 characters!')
        is_valid = False
    if password != confirm:
        flash('Passwords do not match!')
        is_valid = False
    if is_valid:
        flash('Successfully registered')
        parameters = {
                    'first_name': first,
                    'last_name': last,
                    'email': email,
                    'pw_hash': pw_hash
        }
        create_user_sql = 'insert into users (first_name, last_name, email, pw_hash, created_at) values (:first_name, :last_name, :email,:pw_hash, NOW())'
        user_id = mysql.query_db(create_user_sql, parameters)
        setup_session(user_id, email)
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

def setup_session(user_id, email):
    session['user_id'] = user_id
    session['email'] = email


app.run(debug=True)
