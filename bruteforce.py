from schemeA import schemeA
from random import randint, seed
from time import time
from numpy import array, mod, dot

MAXMOD = 65537
O = array([3389, 2969, 3471, 284, 3381, 764, 1914, 1450, 836, 3836, 3691, 1391])
tries = 0
zeros = 3
cnt = 0

while True :
    seed(time())
    V = array([randint(0, MAXMOD) for _ in range(8)])
    A = array([[randint(0, MAXMOD) for _ in range(12)]
                    for _ in range(8)])

    if (schemeA(V, A).all() == O).all():
        break

    tries += 1
    if tries % 10**zeros == 0:
        print(tries)
        cnt += 1
        if cnt == 9:
            cnt = 0
            zeros += 1


print("V =>\n", V, "\nA =>\n", A)