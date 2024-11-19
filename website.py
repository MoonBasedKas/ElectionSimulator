from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def Welcome(name = None):
    return render_template('index.html', person=name)

@app.route("/hi")
def hello():
    return "<p>Hello!</p>"