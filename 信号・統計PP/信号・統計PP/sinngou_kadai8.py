from numpy import *
from matplotlib.pyplot import *

n = linspace(0,4,5)
h = [2,1]
x1 = [1,3]
x2 = [-1,2]

y1 = convolve(h,x1)
y1 = insert(y1,3,[0,0])
y2 = convolve(h,x2)
y2 = insert(y2,0,[0,0])
y = y1+y2

subplot(3,1,1)
stem(n,y1)
ylabel('y1(n)')
subplot(3,1,2)
stem(n,y2)
ylabel('y2(n)')
subplot(3,1,3)
stem(n,y)
ylabel('y(n)')
show()
