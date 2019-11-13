# Library

from numpy import *
from matplotlib.pyplot import *
fileName = 'weightHeightData.csv'
sampleData = loadtxt(fileName,delimiter=',') 
X = sampleData[:,(0,1)]
y = sampleData[:,2]

# Graph
figure(figsize=(6,6)) 
plot(X[y==1,0],X[y==1,1],'bo') 
plot(X[y==-1,0],X[y==-1,1],'rd')
xlabel('Weight [kg]') 
ylabel('Height [cm]')
show()
