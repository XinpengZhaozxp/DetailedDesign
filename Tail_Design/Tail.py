import numpy as np
import scipy.integrate as spi

class Tail():
    _row = 1.002
    _mu = 1.89e-5
    def __init__(self, cr, s, lamb,Name):
        C_r = cr  # This is the root chord length
        b = s    # This is the span
        lam = lamb
        leading_f = lambda x:  -np.tan(np.deg2rad(lamb))*x+cr
        id = Name  # Name of airfoil

        C_t = leading_f(b)   # tip chord length
        y, err = spi.quad(leading_f, 0, b)
        C_bar = (1/b)*y
        S = (C_t+C_r)*b*0.5
        S_total = 4*S
        print("Name")
        print("Root chord length: ", C_r)
        print("Tip chord length: ", C_t)
        print("Mean chord length: ", C_bar)
        print("Single platform area: ", S)
        print("Total platform area: ", S_total)


