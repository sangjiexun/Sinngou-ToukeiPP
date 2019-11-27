from numpy import *
from matplotlib.pyplot import *

n = linspace(-2,5,8)
x = array([0,0,3,2,1,0,0,0])
# (x1,x2)遅延
# mの値が遅延に当たるため
x1 = roll(x,-1)
x2 = roll(x,-2)
# (X1,X2)進相
X1 = roll(x,1)
X2 = roll(x,2)
X3 = roll(x,3)

# 自己相関関数
#表に変換した場合同じ位置での積演算を行いそれぞれ足し合わせた結果が
r = correlate(x,x)
r1 = correlate(x,x1)
r2 = correlate(x,x2)
R1 = correlate(x,X1)
R2 = correlate(x,X2)
R3 = correlate(x,X3)

print(f'x( n )={x} r(m)={r[0]}\nx(n+2)={x2} r(m)={r2[0]}\nx(n+1)={x1} r(m)={r1[0]}\nX( n )={x} r(m)={r[0]}\nx(n-1)={X1} r(m)={R1[0]}\nx(n-2)={X2} r(m)={R2[0]}\nx(n-3)={X3} r(m)={R3[0]}')
#Plot
subplot(6,1,1)
stem(n,x)
ylabel(f'$r(m)={r[0]}$')
subplot(6,1,2)
stem(n,x2)
ylabel(f'$r(m)={r2[0]}$')
subplot(6,1,3)
stem(n,x1)
ylabel(f'$r(m)={r1[0]}$')
subplot(6,1,4)
stem(n,x)
ylabel(f'$r(m)={r[0]}$')
subplot(6,1,5)
stem(n,X1)
ylabel(f'$r(m)={R1[0]}$')
subplot(6,1,6)
stem(n,X2)
ylabel(f'$r(m)={R2[0]}$')
show()
