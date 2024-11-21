import random
import math
from sympy import *
import paillerKeys as pk

"""
public key = n, g
private key = lambda, mu 
We just pass in p and q as private keys they are determined using that.
"""
class paillerObj:

    """ 
    n public key
    g public key
    p private key
    q private key
    """
    def __init__(self, *args):
        self.p = 0
        self.q = 0
        self.g = 0
        self.n = 0
        if len(args) >= 2:
            self.setPublicKey(args[1], args[0])
            if len(args) == 4:
                self.setPrivateKey(args[2], args[3])

    """
    Sets the public key of a given file.
    """
    def setPublicKey(self, g, n):
        self.g = g
        self.n = n
        self.r = random.randint(1,self.n - 1)
        while math.gcd(self.n, self.r) != 1:
            self.r = random.randint(1,self.n - 1)

    def setPrivateKey(self, p, q):
        self.p = p 
        self.q = q
        return
    
    """
    @pt the plain text
    @g our random integer we raise to the power.
    """
    def encrpt(self, pt):
        # g^pt * r^n
        self.cipherText = ((self.g**pt)*(self.r**self.n))
        # ct % n^2
        self.cipherText = self.cipherText % (self.n**2)

    """
    Decrypts the given cipher text and returns the result.
    """
    def decrypt(self):
        # Finds the lcm
        lcm = math.lcm(self.p - 1, self.q - 1)
        k = self.L(self.g**lcm)
        k = k % self.n**2
        mu = self.modInverse(k, self.n)

        pt = self.cipherText**lcm
        pt %= self.n**2
        pt = self.L(pt)
        pt *= mu
        pt %= self.n
        return pt
    

    """
    Determines the L value.
    """
    def L(self, mu): 
        x = mu - 1
        x //= self.n
        
        return x
    
    """
    Multiplies a pailler by a plaintext result pt = pt * new
    """
    def multiply(self, new):
        self.cipherText **= new
        self.cipherText %= self.n**2


    """
    Adds two encrypted paillers together. Must be a 
    paillierObj.
    pt = pt + new
    """
    def add(self, new):
        self.cipherText *= new
        self.cipherText %= self.n**2
    

    """
    Finds the inverse of a modulo
    """
    def modInverse(self, x, y):
        for i in range(1, y):
            if (((x % y) * (i % y)) % y == 1):
                return i
        return -1
    