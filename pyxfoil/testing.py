from pyxfoil.running import running
from pyxfoil.xfoil_analysis import xfoil_analysis
import numpy as np


#path = "D:\\Xinpeng Zhao\\Desktop\\XFOIL6.99\\XFOIL6.99\\"
#running('e475', path, 123456)


Re = np.linspace(600000, 900000, 6)
Re = np.around(Re)
for ele in Re:
    xfoil_analysis('naca2410', ele)


# xfoil_analysis('e475', 666667)

