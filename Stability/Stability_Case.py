import copy
import TailDesign.HorizontalTail as ht
import TailDesign.VerticalTail as vt
import Utility.Utility_Functions as utilf
#from Stability.longtunial import longtunial as long
import numpy as np

class Stability_Case(object):
    # Aircraft specs
    _W = 900 # lb need to use util to convert to N later
    _hnwb = None
    _h = None
    _hn = None # Might need fix
    def __init__(self, argW, arght, argvt, cond):
        self.Wing = copy.deepcopy(argW)
        self.HT =  copy.deepcopy(arght)
        self.VT = copy.deepcopy(argvt)

        # +==================================
        # +         Wing Variables
        # +==================================
        # Values that are assuming constant
        self.S = self.HT.getWingArea()
        self.b = self.HT.getWingSpan()
        # Values that are changing with Re
        self.a = None
        self.a_wb = None
        self.depsdalf = None

        # +==================================
        # +         HT Variables
        # +==================================
        # Values that are assuming constant
        self.S_ht = self.HT.getTotalArea()
        self.Vh = self.HT.Vh
        self.Vh_bar = self.HT.Vh_bar
        # values that are changing with Re
        self.a_ht = None
        self.cma_ht = None

        # +==================================
        # +         long variables
        # +==================================
        self.hn = None
        self.aht = None

        self.CM = None
        self.Cm0 = None
        self.Cm_p = None
        self.Cma = None
        self.Cm_de = None   # need fix
        self.c_mac_wb = None

        self.CL = None
        self.Cla = None     # need to fix later!
        self.Cl_de = None   # need fix
        self.CL_trim = None # need fix

        self.CD = None
        self.Cd0 = None
        self.K = None       # need to connect with CL^2 during calculation

        self.det =None      # crate function for this

        # +==================================
        # +         lat variables
        # +==================================



    # Setters
    def set_lt(self):
        Stability_Case._hn = 0.2
