import paillerKeys
import paillierObj
import provence
import sys
import dbCon as db
import threading
import random

# keys = paillerKeys.paillerKeys(1009, 1013)
keys = paillerKeys.paillerKeys(13, 11)

def main():
    pop = 10000
    # Perhaps have the website write these into an env file just like the database
    # TODO: Write public keys to env file.
    p = 0
    q = 0
    delay = 5
    var = 2
    sys.argv.pop(0) # removes the executable name.
    command = ""
    while len(sys.argv) != 0:
        command = sys.argv[0]
        sys.argv.pop(0)
        if command == "-pop": # set base population
            pop = int(sys.argv.pop(0))
        elif command == "-private": # p,q
            p = int(sys.argv.pop(0))
            q = int(sys.argv.pop(0))
        elif command == "-d":
            delay = int(sys.argv.pop(0))
        elif command == "-v":
            var = int(sys.argv.pop(0))
        elif command == "-clean":
            db.DBCon().clean()
            exit()
        elif command == "-h":
            print("help\n-----")
            print("-bp   [n]:\tModifies the starting port to n.")
            print("-n    [n]:\tmodifies the starting amount of nodes to n.")
            print("-h       :\thelp command.")
            print("-m [mode]:\tThe mode command")
            print("-----")
            print("Shutting down now...")
            exit()
            pass
        else:
            print("Invalid command use -h for help.")
    prov = [["Cramer", 10], ["Fidel", 10], ["Jonesa", 10], ["Jones", 10]]
    keys.generateN()
    keys.generateG()

    setupNormal(prov, keys.g, keys.n, delay, var)
    readResults(keys)
    return 0

def setupNormal(provences, g, n, delay, var):
    threads = []
    while provences != []:
        data = provences.pop(0)
        temp = provence.provence(data[1], data[0], g, n, ["Taco", "Pizza"], [50,50])

        x = threading.Thread(target=temp.runSimulation, args=(delay, var,))
        x.start()
        threads.append(x)
    for t in threads:
        if t != None:
            t.join()


def readResults(key):
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