import numpy as np
import matplotlib.pyplot as plt
fs = 1
f = np.linspace(0.01,0.49,100)
z = np.exp(1j*2*np.pi*f/fs)
X = z/(z-1)**2
fig = plt.figure()
plt.plot(f,20*np.log10(np.abs(X)))
plt.autoscale(enable=True, axis='x', tight=True)
plt.xlabel('f/fs')
plt.ylabel('Magnitude [dB]')
plt.show()
