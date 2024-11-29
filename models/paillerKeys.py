"""
A python object which will generate the agreed upon keys.
"""
import random
import math
from sympy import *
import paillierObj as pObj

class paillerKeys:

    n = 0
    g = 0
    """
    Zero arguements will auto generate
    Two arguements will set those two numbers as keys.
    Four will set all values.
    p,q,g,n
    """
    def __init__(self, *args):
        if (len(args) == 0):
            self.p = 2
            self.q = 2
            while not isprime(self.p):
                self.p = random.randint(2, 10000)
            while not isprime(self.p):
                self.q = random.randint(2, 10000)
        elif (len(args) == 2):
            self.p = args[0]
            self.q = args[1]
        elif (len(args) == 4):
            self.p = args[0]
            self.q = args[1]
            self.g = args[2]
            self.n = args[3]
        else:
            print("Invalid arguements provided")

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
        lim = self.n**2
        q = 0
        while True:
            q = random.randint(2, lim - 1)
            if self.validateG(q):
                self.g = q
                print(q)
                break
        print("key",self.g)
        return self.g

    """
    Just directly test it. A very lazy solution however, this is also significantly
    easier to implement than most other solutions and so far appears to be fairly reliable.
    """
    def validateG(self, g):
        test = random.randint(2,self.n)
        sample = pObj.paillerObj(self.n, g)
        sample.p = self.p
        sample.q = self.q
        test = 2
        sample.encrpt(test)
        z = sample.decrypt()
        print("testing", z, test, "on", g)
        if z == test:
            print(g, "was a good choice")
            return True
        return False

    
    """
    Determines the L value.
    """
    def L(self, mu): 
        x = mu - 1
        x //= self.n
        
        return x
    
    """
    Finds the inverse of a modulo
    """
    def modInverse(self, x, y):
        for i in range(1, y):
            if (((x % y) * (i % y)) % y == 1):
                return i
        return -1

        # lim = (self.p - 1) * (self.q - 1)
        # for j in range(2, self.n ** 2):
        #     early = False
        #     hits = []
        #     self.g = j
        #     for i in range(self.n**2):
        #         # It seems to just set g if it fails the test.
        #         temp = (self.g**i) % (self.n**2)
        #         if temp in hits:
        #             print(self.g, "Key failed at", i)
        #             early = True
        #             break
        #         hits.append(temp) # This is going to be slow.

        #     if early:
        #         pass
        #     else:
        #         processing = False
        return self.g
    

    def findTotient(self):
        count = 0
        target = self.n**2
        for i in range(1, target):
            if math.gcd(i, target) == 1:
                count += 1
        return count
    

    def getTotientPrimes(self, totient):
        primes = []
        for i in range(2, totient):
            if isprime(i) and totient % i == 0:
                primes.append(i)
        return primes
    
    def getPrivateP(self):
        return self.p
    
    def getPrivateP(self):
        return self.q


keys = paillerKeys(113,97)
keys.generateN()
keys.generateG()
# keys.g = keys.n + 1

z = pObj.paillerObj(keys.n, keys.g) # Bad g != 8892
z.encrpt(99)
z.p = 113
z.q = 97
print(z.decrypt())
# x = paillerObj(247, 16477)
# x = paillerObj(247, 33572) # Bad g
x = pObj.paillerObj(keys.n, keys.g) # Bad g
x.encrpt(147)
z.add(x.cipherText)
print(z.decrypt())