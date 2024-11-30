from flask import Flask
from flask import render_template
from models import dbCon, main, paillierObj, paillerKeys





from flask import Flask, jsonify, request
keys = paillerKeys.paillerKeys() # Update this
db = dbCon.DBCon() # Connect to the database
app = Flask(__name__)


# @app.route('/home')
# def Welcome(name = None):
#     return render_template('index.html', person=name)

@app.route('/')
@app.route('/home')
def Welcome():
    return render_template('home.html')

@app.route('/start', methods=['GET'])
def Welcome():
    db.clean() # Clean out old results if any
    args = [] # Simulation args
    
    return render_template('start.html')

@app.route('/homomorphism')
def homo():
    return render_template('viewEnc.html')

@app.route('/voting')
def vote():
    return render_template('votePannel.html')


"""
Old and outdated will remove and just rely upon jynxy
"""
@app.route('/api/data', methods=['GET', 'POST'])  
def api_data():
    if request.method == 'POST':
        data = request.json  
        print('Received JSON data:', data)
        return 'JSON data received successfully!', 200
    elif request.method == 'GET':
            db = dbCon.DBCon()
            z = db.fetchVotesEnc()
            json_data = {}
            ids = []
            for i in z:
                ids.append(i.id)
                json_data[i.id] = {'Canidate':i.canidate, 'Location':i.location,'Votes':i.count}
            json_data[-1] = ids
    return jsonify(json_data)

@app.route("/hi")
def hello():
    return "<p>Hello!</p>"