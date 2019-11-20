# Library
from numpy import *
from matplotlib.pyplot import *
from sklearn.svm import SVC 

fileName = 'Data/weightHeightData.csv'
sampleData = loadtxt(fileName,delimiter=',') 
X = sampleData[:,(0,1)]
y = sampleData[:,2]
svm = SVC(kernel='linear',C = 1.0)
svm.fit(X[0],X[1])
re = svc.predict(y)
print(re)

# Graph
figure(figsize=(6,6)) 
plot(X[y==1,0],X[y==1,1],'bo') 
plot(X[y==-1,0],X[y==-1,1],'rd')
xlabel('Weight [kg]') 
ylabel('Height [cm]')
grid()
show()

