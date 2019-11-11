from numpy import *
from matplotlib.pyplot import *

Ts = 1
xMin = 0.01
xMax = 0.5
N = 100   #データ密度
n = 0
f = linspace(xMin,xMax,N)
z = exp(1j*2*pi*f/Ts)
A = [0.5],[1.0],[2.0]
H = 25*log10(abs(1/(1-A*z**(-1)))) #ベクトル計算
for h in H:
	plot(f,h,label=str(*A[n]))
	n += 1
xlim(xMin,xMax)
ylim(-12,30)
xlabel('F/Ts')
ylabel('Magnitude [db]')
legend()
show()