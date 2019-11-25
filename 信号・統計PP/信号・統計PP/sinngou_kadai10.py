from numpy import *
from matplotlib.pyplot import *

n = linspace(-2,5,8)
x = array([0,0,3,2,1,0,0,0])
#(x1,x2)遅延+
x1 = roll(x,-1)
x2 = roll(x,-2)
#(X1,X2)遅延-
X1 = roll(x,1)
X2 = roll(x,2)

r = correlate(x,x)
r1 = correlate(x,x1)
r2 = correlate(x,x2)
R1 = correlate(x,X1)
R2 = correlate(x,X2)
print(f'x( n )={x} r(m)={r[0]}\nx(n+2)={x2} r(m)={r2[0]}\nx(n+1)={x1} r(m)={r1[0]}\nX( n )={x} r(m)={r[0]}\nx(n-1)={X1} r(m)={R1[0]}\nx(n-2)={X2} r(m)={R2[0]}\n')
