from TailDesign.Tail import Tail
import numpy as np
import scipy.integrate as spi


class HorizontalTail (Tail):
    def __init__(self, cr, b, lamb, Name):
        Tail.__init__(self, cr, b, lamb, Name)
        self.Vh_bar = (self.S_t_total * Tail._lt_bar) / (Tail._S_w * 1.42)
        self.Vh = (self.S_t_total*Tail._lt)
        Tail.info(self)
        print("Horizontal Tail Volume Ratio(bar)", self.Vh_bar,"\n")

    def getTotalArea(self):
        return self.S_t_total;