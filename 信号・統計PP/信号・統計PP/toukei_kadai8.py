# Library
from numpy import *
from matplotlib.pyplot import *
from sklearn import *

fileName = 'Data/weightHeightData.csv'
sampleData = loadtxt(fileName,delimiter=',') 
X = sampleData[:,(0,1)]
y = sampleData[:,2]
data = SVM(kernel='X')

# Graph
figure(figsize=(6,6)) 
plot(X[y==1,0],X[y==1,1],'bo') 
plot(X[y==-1,0],X[y==-1,1],'rd')
xlabel('Weight [kg]') 
ylabel('Height [cm]')
show()

