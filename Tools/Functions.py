import numpy as np
from Tail_Design import Tail


def reNum(u, row=1.002, mu=1.89e-5 ,L=0.51184):
    return (row*u*L)/mu


def VelocityFromRe(Re, row=1.002, mu=1.89e-5, l=0.51184):
    return (Re*mu)/(row*l)

def vConv(u,s1,s2):
    if s1=='ft':
        if s2 == 'm':
            return u*0.3048
        if s2 == 'kt':
            return u*0.592484
    elif s1 == 'm':
        if s2 == 'ft':
            return u*3.28084
        if s2 == 'kt':
            return u*1.943848
    else:
        if s2 == 'm':
            return u*0.51444
        if s2 == 'ft':
            return u*1.68781


Re1 = 3e6  # local mission: 83.33m/s
Re2 = 2.1e6 # logistic mission 58.33m/s
Re3 = 407034 # potential transition speed 15m/s


leadingEdgeEq_1 = lambda x:  -np.tan(np.deg2rad(10))*x+0.6
HT = Tail.Tail(0.6, 1, 10, leadingEdgeEq_1, "Horizontal")


print(reNum(66.8))

L = 1.41*0.5*1.002*58.333**2*1.0237
M = L*1.3
print(L)
print(M)




