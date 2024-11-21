"""
Manages querrying the database however the we do not have to make a lot of queries 
so this is a rather lightweight class.
"""
import mysql.connector
import vote

class DBCon:
    def __init__(self):
        fp = open("/home/kas/.env/DBE_CONFIG" ,"r")
        lines = fp.readlines()
        user = lines[0].split("=")[1].strip()
        password = lines[1].split("=")[1].strip()
        self.cnx = mysql.connector.connect(user=user, password=password,
                                host='127.0.0.1',
                                database='votes')
        self.cursor = self.cnx.cursor()

    """
    Inserts votes into the database.
    Vote format is candiate, origin, quantity.
    """
    def insertVotes(self, *args):
        if len(args) != 3:
            print("Error | Invalid args provided.")
            return 

        query = ('insert into voteTable (canidate, origin, votes) values (%s, %s, %s)')
        self.cursor.execute(query, (args[0], args[1], args[2]))
        self.cnx.commit()

    """
    Fetches the votes from the database and returns their all votes.
    """
    def fetchVotes(self):
        query = ('select * from voteTable')
        values = []
        self.cursor.execute(query, ())
        for (i, c, o, t) in self.cursor:
            values.append(vote.vote(i, c,o,t))
        return values
    
    def closeDB(self):
        self.cursor.close()
        self.cnx.close()