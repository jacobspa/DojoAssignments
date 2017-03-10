from flask import Flask, flash, redirect, render_template, request, session
import re
app = Flask(__name__)
app.secret_key = "ThisIsTheSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/authentication", methods=['POST'])
def authentication():
    print "I am here!"
    print request.form['html_email'], request.form['html_first'], request.form['html_pass']
    if len(request.form['html_email']) < 1:
        flash("Email Cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['html_email']):
        flash("Email is not valid")
    if len(request.form['html_first']) < 1:
        flash("First Name Cannot be empty!")
    if len(request.form['html_last']) < 1:
        flash('Last Name Cannot be empty!')
    if any(char.isdigit() for char in request.form['html_first']):
        flash('First name cannot contain any numbers')
    if any(char.isdigit() for char in request.form['html_last']):
        flash("Last name cannot contain any numbers")
        print "I got here"
    if len(request.form['html_pass']) < 1:
        flash('Password Cannot be empty!')
    if len(request.form['html_confirm']) < 1:
        flash('Must Confirm Password!')
        print "I am here"
    if len(request.form['html_pass']) < 8:
        flash("Password must be longer than 8 characters")
    if request.form['html_pass'] == request.form['html_confirm']:
        print "Passwords to not match"
        flash('Passwords do not match!!!')
    else:
        print "else"
        server_first = request.form['html_first']
        server_last = request.form['html_last']
        server_email = request.form['html_email']
        server_pass = request.form['html_pass']
    return redirect('/')
app.run(debug=True)
