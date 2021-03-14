from TailDesign.Tail import Tail
import numpy as np
import scipy.integrate as spi

class VerticalTail(Tail):
    def __init__(self, cr, b, lamb, Name):
        Tail.__init__(self, cr, b, lamb, Name)
        self.Vv = (self.S_t_total * Tail._lf_class) / (Tail._S_w * Tail._b)
        Tail.info(self)
        print("Vertical Tail Volume Ratio", self.Vv, "\n")