from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'world')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
print mysql.query_db("SELECT * FROM countries")
app.secret_key= 'thisIsSecret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if not EMAIL_REGEX.match(request.form['html_email']):
        flash('The email is NOT valid!')
    else:
        return redirect('/')



app.run(debug=True)
