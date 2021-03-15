import Stability.Stability_Case as sc
import TailDesign.HorizontalTail as ht
import TailDesign.VerticalTail as vt
import Utility.Utility_Functions as util
import numpy as np

Hori_t = ht.HorizontalTail(1.2, 1.3, 10, "e475")
Vertical_t = vt.VerticalTail(1.3, 0.88, 30, "e475")
foowing = 0


case1=sc.Stability_Case(foowing, Hori_t, Vertical_t, 0)
