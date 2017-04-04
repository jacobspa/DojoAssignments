from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'Mesopotamia')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# print mysql.query_db("SELECT * FROM emails")
app.secret_key= 'thisIsSecret'

@app.route('/')
def home():
    # print mysql.query_db("SELECT * FROM emails")
    all_users = mysql.query_db('select * from emails')
    all_users= all_users[0]['email']


    return render_template('index.html',user_id=all_users)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if not EMAIL_REGEX.match(request.form['html_email']):
        flash('The email is NOT valid!')
        server_email = request.form['html_email']
    else:
        query ='INSERT INTO emails(email) VALUES(:email)'
        data = {
                'email': request.form['html_email'],
                }
        user_id = mysql.query_db(query, data)
        return redirect('/')



app.run(debug=True)
