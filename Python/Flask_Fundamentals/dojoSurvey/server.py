from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="ThisIsSecret"


@app.route('/')
def survey():
    return render_template("survey.html")
    flash

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return render_template('result.html')
    elif (len(request.form['comment']) < 1) or (len(request.form['comment']) > 121):
        flash("Comment must be between 0 and 120 characters!")
        return render_template('result.html')
    else:
        name = request.form['name']
        location = request.form['location']
        comment = request.form['comment']
        return render_template('result.html', name=name, location=location, comment=comment)




app.run(debug=True)
