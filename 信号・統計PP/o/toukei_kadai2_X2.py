import numpy as np 
import scipy.stats as st
import matplotlib.pyplot as plt

def drawVLine(zl,zh,pdf,lineColor):
     Z = np.linspace(zl,zh,300)     
     for z in Z:         
         lineX = z*np.ones(2)         
         lineY = np.array([0.0,pdf(z)])         
         plt.plot(lineX,lineY,c=lineColor)
         
alpha = 0.99
DF = 5
gxmin,gxmax = (0,20)

rv = st.chi2(df=DF) 
x = np.linspace(gxmin,gxmax,100) 
f = rv.pdf(x) 

x1 = rv.isf((1+alpha)/2) 
print('x2=%.3f' % x1) 
x2 = rv.isf((1-alpha)/2) 
print('x2=%.3f' % x2) 

plt.figure(figsize=(6,4)) 
plt.plot(x,f) 
plt.autoscale(tight=True) 

drawVLine(x1,x2,rv.pdf,'r') 
plt.show() 
