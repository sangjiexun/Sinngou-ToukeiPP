# Library

from numpy import *
from matplotlib.pyplot import *
from svm import *
#from sklearn.svm import SVC
fileName = 'Data/weightHeightData.csv'
sampleData = loadtxt(fileName,delimiter=',') 
x = sampleData[:,(0,1)]
y = sampleData[:,2]
svm = SVC(gamma='auto')
#svm.fit(a[])

xmin = min(x[:,(0)])
xmax = max(x[:,(0)])
X = linspace(xmin,xmax,1000)
#x2=ax1+b
w0 = -37.0346
w1 = 0.2776
w2 = 0.1248
a = -(w1/w2)
b = -(w0/w2)
Y = (a*X+b)
# Graph
figure(figsize=(6,6)) 

plot(x[y==1,0],x[y==1,1],'bo',label = 'man') 
plot(x[y==-1,0],x[y==-1,1],'rd',label = 'woman')
plot(X,Y,label = 'x2=ax2+b')
xlabel('Weight [kg]') 
ylabel('Height [cm]')
autoscale(enable=True,axis='x',tight=True)
legend()
grid()
show()
