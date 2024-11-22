from flask import Flask
from models import dbCon
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def Welcome(name = None):
    return render_template('index.html', person=name)

from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
@app.route('/api/data', methods=['GET', 'POST'])  
def api_data():
    if request.method == 'POST':
        data = request.json  
        print('Received JSON data:', data)
        return 'JSON data received successfully!', 200
    elif request.method == 'GET':
           db = dbCon.DBCon()
           z = db.fetchVotesEnc()
           for i in z:
                json_data = {}
                json_data[i.id] = {'Canidate':i.canidate, 'Location':i.location,'Votes':i.count}

    return jsonify(json_data)

@app.route("/hi")
def hello():
    return "<p>Hello!</p>"