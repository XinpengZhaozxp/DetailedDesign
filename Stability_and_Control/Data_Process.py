import numpy as np

Re200k = np.loadtxt("Re200k.txt", skiprows=12)
ind, dum = np.where(Re200k[:, 0:1]==0)
C_l_alpha = (Re200k[ind+1, 1]-Re200k[ind-1,1])/np.deg2rad(Re200k[ind+1, 0]-Re200k[ind-1, 0])
C_m_alpha = (Re200k[ind+1, 4]-Re200k[ind-1, 4])/np.deg2rad(Re200k[ind+1, 0]-Re200k[ind-1, 0])
X_ac_t = 0.25-(C_m_alpha/C_l_alpha)
