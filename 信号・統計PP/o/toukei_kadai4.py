import numpy as np
import matplotlib.pyplot as plt 


x = np.array([86,71,42,62,96,39,50,78,51,89])
n = len(x)
siguma2 = np.var(x,ddof=1)
line = np.linspace(0,100,100)
sum = 0

LL = -n/2*np.log(2*np.pi*siguma2)
for i in range(n):
	LL -= ((x[i]-line)**2)/(2*siguma2)

print('n =',n,'mean =',np.mean(x))

plt.figure()
plt.plot(line,LL)
plt.xlabel('μ')
plt.ylabel('Log Likelihood')
plt.xlim(0,100)
plt.ylim(-100,-40)
plt.vlines(np.mean(x),-100,0,colors='r',linestyle='dashed')
plt.show()