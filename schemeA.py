from random import randint, seed
from time import time
from numpy import array, mod, dot

MAXMOD = 65537

def schemeA(V, A) :
    o = mod(dot(V, A), MAXMOD) // 16
    return o

if __name__ == '__main__':
    seed(time())
    V = array([randint(0, MAXMOD) for _ in range(8)])
    A = array([[randint(0, MAXMOD) for _ in range(12)]
                 for _ in range(8)])
    
    print("V =>\n", V)
    print("A =>")
    for i in range(len(A)):
        print("", A[i])
    print("o =>\n", schemeA(V, A))