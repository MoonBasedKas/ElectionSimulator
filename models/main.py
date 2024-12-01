from models import paillerKeys
from models import paillierObj
from models import provence
import sys
from models import dbCon as db
import threading
import random

def main():
    sys.argv.pop(0) # removes the executable name.
    startSimulation(sys.argv)


"""
Starts the simulation itself. Inputs a list structured as if they were command line arguments.
"""
def startSimulation(args):
    print(args)
    pop = 10000
    p = 0
    q = 0
    g = 0
    delay = 3
    var = 2
    command = ""
    while len(args) != 0:
        command = args[0]
        args.pop(0)
        if command == "-pop": # set base population
            pop = int(args.pop(0))
        elif command == "-private": # p,q
            p = int(args.pop(0))
            q = int(args.pop(0))
        elif command == "-public":
            g = int(args.pop(0))
        elif command == "-d":
            delay = int(args.pop(0))
        elif command == "-v":
            var = int(args.pop(0))
        elif command == "-clean":
            db.DBCon().clean()
            exit()
        elif command == "-h":
            print("Read the code or something...")
            print("Shutting down now...")
            exit()
            pass
        else:
            print("Invalid command use -h for help.")
    if p == 0 or q == 0: # This should never be called
        keys = paillerKeys.paillerKeys()
        keys.generateN()
        keys.generateG()
        
    else:
        keys = paillerKeys.paillerKeys(p, q)
        keys.generateN()
        if g == 0:
            keys.generateG()
        else:
            keys.g = g
        
    prov = [["Cramer", pop//7], ["Fidel", pop//7], ["Jonesa", pop//7], ["Jones", pop//7]]
    prov.append(["Wier", pop//7])
    prov.append(["Speare", pop//7])
    prov.append(["Workman", pop//7])
    # print(keys.g, keys.n)
    setupNormal(prov, keys.g, keys.n, delay, var)
    # readResults(keys)
    return keys # Return generated keys


"""
Creates the threads to begin sending their votes.
"""
def setupNormal(provences, g, n, delay, var):
    threads = []
    while provences != []:
        data = provences.pop(0)
        temp = provence.provence(data[1], data[0], g, n, ["Taco", "Pizza"], [50,50])

        x = threading.Thread(target=temp.runSimulation, args=(delay, var,), name=data[0])
        x.start()
        threads.append(x)
    return 

"""
Prints out the results of the election.
"""
def readResults(keys):
    taco = paillierObj.paillerObj(keys.n, keys.g, keys.p, keys.q)
    pizza = paillierObj.paillerObj(keys.n, keys.g, keys.p, keys.q)
    pizza.cipherText = -1
    taco.cipherText = -1
    p = 0
    t = 0
    res = db.DBCon().fetchVotesEnc()
    for i in res:
        if i.canidate == "Pizza":
            if pizza.cipherText == -1:
                pizza.cipherText = i.count
            else:
                pizza.add(i.count)
        else:
            if taco.cipherText == -1:
                taco.cipherText = i.count
            else: 
                taco.add(i.count)
    
    res = db.DBCon().fetchVotesPT()
    for i in res:
        if i.canidate == "Pizza":
            p += i.count
        else:
            t += i.count

    print("Pizza Votes:", pizza.decrypt(), p)
    print("Taco Votes:", taco.decrypt(), t)





if __name__ == "__main__":
    main()