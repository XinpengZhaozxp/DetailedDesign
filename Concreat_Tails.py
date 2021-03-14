import TailDesign.HorizontalTail as ht
import TailDesign.VerticalTail as vt
import Tools.Utility as util
import numpy as np

Hori_t = ht.HorizontalTail(1.2, 1.3, 10, "Horizontal(E-451)")
Vertical_t = vt.VerticalTail(1.3, 0.88, 30, "Vertical(E-451)")
u = np.linspace(15, 90, 15)
ReH = util.reNum(u, Hori_t.C_bar)
ReV = util.reNum(u, Vertical_t.C_bar)
Re = np.linspace(200000, 2500000, 15)