"""
This is mostly just a container for votes.
"""

class vote:

    def __init__(self, id, canidate, location, count):
        self.id = id
        self.canidate = canidate
        self.location = location 
        self.count = count