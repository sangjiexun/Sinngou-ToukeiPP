#演習問題 9
from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *
# データの読み込み
fileName = 'Data/examResult2.csv'
data = loadtxt(fileName, delimiter=',',usecols=(1,2,3,4))
X = data[:,(0,1)].T
(M,K)=X.shape
print(X)
# PCA
C = cov(X)
w,A = eig(C)
index = argsort(w)
rindex = index[array(range(M-1,-1,-1))]
w = w[rindex] # 降順に並べ替え
A = A[:,rindex] # 降順に並べ替え
Z = dot(A[:,0].T,X) # 第１主成分
print('Z=',Z)
x = linspace(0,0,10)
n = arange(1,10)
title('First main component')
for Z_,x_,n_ in zip(Z,x,n):
	plot(Z_,x_,'o',color='b')
	annotate(n_,xy=(Z_,x_))
show()
