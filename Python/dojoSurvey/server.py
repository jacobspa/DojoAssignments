from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def survey():
    return render_template("survey.html")

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, comment=comment)


app.run(debug=True)
