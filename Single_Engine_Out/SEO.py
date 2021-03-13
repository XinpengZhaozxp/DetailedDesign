import numpy as np
import matplotlib.pyplot as plt

Aht = 0.515*3
Avt = 0.919*3
clh = 1.44
clv = 0.9
lh = 0.4
lv = 0.3
row = 1.002

speed = np.linspace(0, 50, 200)
torque = 0.5*row*pow(speed, 2)*clh*Aht*lh+0.5*row*pow(speed, 2)*clv*Avt*lv

plt.figure()
plt.plot(speed, torque)
plt.title("Moment VS Downwash Speed")
plt.xlabel("m/s")
plt.ylabel("N*m")
plt.show()