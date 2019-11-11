import numpy as np
import matplotlib.pyplot as plt
E = 5
R = 100
L = 1e-6
t = np.linspace(0,1e-3,100)
i = E/R*(1-np.exp(-R/L*t))
fig=plt.figure()
plt.plot(t*1000,i)
plt.xlabel('Time [ms]')
plt.ylabel('Current [A]')
plt.show()