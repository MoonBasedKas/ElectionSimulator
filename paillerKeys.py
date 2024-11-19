import random
import math
from sympy import *

class paillerKeys:

    n = 0
    g = 0

    def __init__(self, *args):
        if (len(args) == 0):
            self.p = 2
            self.q = 2
            while not isprime(self.p):
                self.p = random.randint(2, 1000000)
            while not isprime(self.p):
                self.q = random.randint(2, 1000000)
        else:
            self.p = args[0]
            self.q = args[1]

    """
    Generates the first public key n for encryption.
    """
    def generateN(self):
        self.n = self.q*self.p
        return self.q * self.p
    
    """
    Generates the second public key g for encryption.
    Somewhere in range of 2->n**2 and is invertible when raised to a
    power.
    """
    def generateG(self):
        processing = true
        while processing:
            self.g = random.randint(2,self.n**2 - 1)
            for i in range(self.n**2):
                if (self.g**i) % (self.n**2) == 1:
                    processing = false
                    break
        return self.g
