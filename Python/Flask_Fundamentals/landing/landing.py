from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("hello.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route("/dojos/new")
def dojos_new():
    return render_template("dojo.html")

app.run(debug=True)
