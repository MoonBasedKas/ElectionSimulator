import paillerKeys
import provence
import sys
import os
import threading
import random


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
        if command == "-pop":
            pop = int(sys.argv.pop(0))
        elif command == "-p":
            p = int(sys.argv.pop(0))
        elif command == "-q":
            q = int(sys.argv.pop(0))
        elif command == "-d":
            delay = int(sys.argv.pop(0))
        elif command == "-v":
            var = int(sys.argv.pop(0))
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
    prov = [["Cramer", 2500], ["Fidel", 2500], ["Jonesa", 2500], ["Jones", 2500]]
    keys = paillerKeys.paillerKeys(113, 117)
    keys.generateN()
    keys.generateG()

    setupNormal(prov, keys.g, keys.n, delay, var)
    return 0

def setupNormal(provences, g, n, delay, var):

    while provences != []:
        data = provences.pop(0)
        temp = provence.provence(data[1], data[0], g, n, ["Taco", "Pizza"], [50,50])

        threading.Thread(target=temp.runSimulation, args=(delay, var,)).start()



if __name__ == "__main__":
    main()