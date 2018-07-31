import numpy as np


class Perceptron:

    def __init__(self):
        pass

    def AND(self,x,y):
        k = 0.5*x+0.5*y-0.7
        if k <= 0:
            return 0
        else:
            return 1

    def OR(self,x,y):
        k = 0.5*x+0.5*y-0.3
        if k <= 0:
            return 0
        else:
            return 1

    def NAND(self,x,y):
        k = 0.5*x+0.5*y-0.7
        if k <= 0:
            return 1
        else:
            return 0
        

    def XOR(self,x,y):
        p = Perceptron()
        s1 = p.NAND(x,y)
        s2 = p.OR(x,y)
        s = p.AND(s1,s2)
        return s


p = Perceptron()
print("OR")
print(p.OR(0,0))
print(p.OR(0,1))
print(p.OR(1,0))
print(p.OR(1,1))
print("AND")
print(p.AND(0,0))
print(p.AND(0,1))
print(p.AND(1,0))
print(p.AND(1,1))
print("NAND")
print(p.NAND(0,0))
print(p.NAND(0,1))
print(p.NAND(1,0))
print(p.NAND(1,1))
print("XOR")
print(p.XOR(0,0))
print(p.XOR(0,1))
print(p.XOR(1,0))
print(p.XOR(1,1))

