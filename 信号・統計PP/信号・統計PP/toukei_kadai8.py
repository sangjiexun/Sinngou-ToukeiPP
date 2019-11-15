# Library
from numpy import *
from matplotlib.pyplot import *
from sklearn.svm import *

fileName = 'Data/weightHeightData.csv'
sampleData = loadtxt(fileName,delimiter=',') 
X = sampleData[:,(0,1)]
y = sampleData[:,2]
xmin = min(X[:,(0)])
xmax = max(X[:,(0)])
x = linspace(xmin,xmax,1000)

#SVM
svm = SVC(kernel = 'linear').fit(X, y)
print(f'w = {svm.coef_},w0 = {svm.intercept_}')
w0 = svm.intercept_
w1 = svm.coef_[0,0]
w2 = svm.coef_[0,1]

a = -(w1/w2)
b = -(w0/w2)
Y = (a*x+b)

# Graph
figure(figsize=(6,6)) 
plot(X[y==1,0],X[y==1,1],'bo',label = 'man') 
plot(X[y==-1,0],X[y==-1,1],'rd',label = 'woman')
plot(x,Y,label = '$x_{2}=%.4fx_{1}+%.4f$'% (a,b))
xlabel('Weight [kg]') 
ylabel('Height [cm]')
legend()
grid()
show()

