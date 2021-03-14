import numpy as np
import scipy.integrate as spi


class Tail(object):
    _lt_bar = 2.5
    _lt = 1.89
    _lf_class = 2.5
    _S_w = 13.46
    _b = 5
    _row = 1.002
    _mu = 1.89e-5

    def __init__(self, cr, b, lamb, Name):
        self.id = Name  # Name of airfoil
        self.C_r = cr  # root chord length
        self.b = b  # This is the span
        self.leading_f = lambda x: -np.tan(np.deg2rad(lamb)) * x + cr
        self.C_t = self.leading_f(self.b)  # tip chord length
        self.y, err = spi.quad(self.leading_f, 0, b)
        self.C_bar = (1 / self.b) * self.y
        self.S_t = (self.C_t + self.C_r) * self.b * 0.5
        self.S_t_total = 4 * self.S_t
        self.X_ac_bar = 0.15 * self.C_bar

        self.Re = None

    def setRe(self, x):
        self.Re = x

    def info(self):
        print(self.id)
        print("Root chord length: ", self.C_r)
        print("Tip chord length: ", self.C_t)
        print("Mean chord length: ", self.C_bar)
        print("Span length: ", self.b)
        print("Single platform area: ", self.S_t)
        print("Total platform area: ", self.S_t_total)
        print("Mean aerodynamic center form leading edge: ", self.X_ac_bar)

    def getWingArea(self):
        return Tail._S_w
