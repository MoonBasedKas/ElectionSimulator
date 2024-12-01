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

"""
Directing to this page will update the keys and start the simulation
"""
@app.route('/start', methods=['GET'])
def start():
    db.clean() # Clean out old results if any
    args = [] # Simulation args
    pop = request.args.get('pop', "10000")
    p = request.args.get('p', "1")
    q = request.args.get('q', "1")
    g = request.args.get('g', "1")
    delay = request.args.get('delay', "1")
    if pop != "":
        pop = int(pop)
        if pop != 10000:
            args.append("-pop")
            args.append(pop)
    if p != "" and q != "":
        p = int(p)
        q = int(q)
        if p > 1 and q > 1:
            args.append("-private")
            args.append(p)
            args.append(q)
            if g != "":
                g = int(g)
                if g > 1:
                    args.append("-public")
                    args.append(g)    
    if delay != "":
        delay = int(delay)
        if delay > 1:
            args.append("-d")
            args.append(delay)
    
    # Place into call args

    

    
    global keys 
    keys = main.startSimulation(args) # Load arguments as if cmd line args
    print(keys.g, keys.n, keys.p, keys.q)
    return render_template('start.html') # Forward to new page

@app.route('/homomorphism')
def homo():
    return render_template('viewEnc.html')

@app.route('/voting')
def vote(vote = None):
    names = ["Cramer", "Jones", "Jonesa", "Fidel", "Speare", "Wier", "Workman"]
    votes = []
    for i in names:
        # location, taco, pizza, percent
        votes.append([i, -1, -1, 50, "Neither"])
    data = db.fetchVotesEnc()
    # Apply the homomorphic calculations
    for j in data:
        for i in votes:
            if i[0] == j.location:
                if j.canidate == "taco":
                    if i[1] == -1:
                        i[1] = j.votes
                    else:
                        i[1] = (i[1] * j.votes) % keys.n**2
                elif j.canidate == "pizza":
                    if i[2] == -1:
                        i[2] = j.votes
                    else:
                        i[2] = (i[2] * j.votes) % keys.n**2
                break
    # Decrypt
    temp = paillierObj.paillerObj(keys.n, keys.g)
    temp.p = keys.p
    temp.q = keys.q
    for j in votes:
        print(votes)
        # CLear
        if j[1] != -1:
            temp.cipherText = j[1]
            j[1] = temp.decrypt()
        else:
            j[1] = 0

        if j[2] != -1:
            temp.cipherText = j[2]
            j[2] = temp.decrypt()
        else:
            j[2] = 0
        
    
    for j in votes:
        total = j[1] + j[2]
        if total != 0:
            percent = j[1] // total
            j[3] = percent
            if j[1] > j[2]:
                j[4] = "Taco"
            elif j[2] > j[1]:
                j[4] = "Pizza"

                        

    return render_template('votePannel.html', vote = votes)


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