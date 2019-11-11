import numpy as np
import matplotlib.pyplot as plt
N = 100
t = np.linspace(0,2,N)
x = np.sin(2*np.pi*t)
plt.figure(figsize = (6,4))
plt.plot(t,x)
plt.xlabel('Time [s]')
plt.show()
plt.savefig('sine.png',format='png') 

