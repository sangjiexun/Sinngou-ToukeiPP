import numpy as np
import matplotlib.pyplot as plt
N=100
B = np.zeros(N)
for n in range(N):
    nn = n+1
    B[n] = 4*(1*-1*(-1**nn))/(nn*np.pi)
plt.figure(figsize=(6,4))
plt.bar(range(N), B)
plt.xlabel("n")
plt.ylabel('B[n]') 
plt.show()
