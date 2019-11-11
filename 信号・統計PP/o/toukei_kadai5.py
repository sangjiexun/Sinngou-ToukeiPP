# 例題5-1
from numpy import *
from scipy.stats import *
from matplotlib.pyplot import *


# データ
data = loadtxt('Data/SnackWeight.csv',delimiter=',')
n=data.size

# 統計量
xBar=mean(data)
S2 = var(data,ddof=0)
S = sqrt(S2)
gamma = 0.99
print('xBar=%.4f'%xBar, ' S2=%.4f'%S2, ' S=%0.4f'%S) 
print('gamma=%.2f'%gamma)

# 母平均
rv = t(df=n-1)
t1 = rv.isf((1-gamma)/2)
theta_L = xBar - S/sqrt(n-1)*t1 
theta_H = xBar + S/sqrt(n-1)*t1 
print("\n母平均")
print('t1=%.4f'%t1 ) 
print('L=%.4f'%theta_L, ' H=%.4f'%theta_H)

# 平均値のグラフ
figure(figsize=(6,4))
gxmin, gxmax = (-4,4) 
gymin,gymax = (0.0, 0.4)
x = linspace(gxmin,gxmax,100) 
f = rv.pdf(x)
plot(x,f)
ylim(gymin,gymax) 
vlines(t1,gymin,gymax,colors='g',linestyles='dashed') 
vlines(t1,gymin,gymax,colors='g',linestyles='dashed')

# 分散
rv = chi2(df=n-1)
x1 = rv.isf((1+gamma)/2) 
x2 = rv.isf((1-gamma)/2) 
theta_L = n*S2/x2 
theta_H = n*S2/x1 
print("\n分散")
print('x1=%.4f'%x1,' x2=%.4f'%x2) 
print('L=%.4f'%theta_L, ' H=%.4f'%theta_H)

# 分散のグラフ
figure(figsize=(6,4))
gxmin, gxmax = (0,30) 
gymin,gymax = (0.0, 0.12)
x = linspace(gxmin,gxmax,100) 
f = rv.pdf(x)
plot(x,f)
ylim(gymin,gymax) 
vlines(x1,gymin,gymax,colors='g',linestyles='dashed') 
vlines(x2,gymin,gymax,colors='g',linestyles='dashed')
show()