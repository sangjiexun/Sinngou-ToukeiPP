from numpy import *
from scipy.stats import *
from matplotlib.pyplot import *
import scipy.stats as st

datax = loadtxt('Data/BMIstrat.csv',delimiter=',') 
datay = loadtxt('Data/BMIsixmonth.csv',delimiter=',')   
m=datax.size
n=datay.size
Sx = std(datax)
Sy = std(datay)
S = Sx**2
print('標準偏差x',S)
S = Sy**2
print('標準偏差y',S)
X = average(datax)
Y = average(datay)
print('平均値x',X)
print('平均値y',Y)
rv = f(m-1,n-1)
gmax = 0.0
gmin = 8.0
z = linspace(gmin,gmax,num=100)
fig=figure(figsize=(6,4))
subplot(2,1,1)
plot(z,rv.pdf(z))
t = rv.isf(0.005)
vlines(t, 0.0,1.0,colors='r',linestyles='dotted')
print('上側棄却域',t)
t = rv.isf(0.995)
vlines(t, 0.0,1.0,colors='r',linestyles='dotted')
print('下側棄却域',t)
T = (m*(n-1))/((m-1)*n)*(Sx**2/Sy**2)
vlines(T, 0.0,1.0,colors='g',linestyles='dashed')
print('検定統計量',T)
title('Dispersion:F-distribution')

gmax = -4.0
gmin = 4.0
z = linspace(gmin,gmax,num=100)
rvt = st.t(df=n+m-2)
subplot(2,1,2)
plot(z,rvt.pdf(z))
t = rvt.isf(0.005)
vlines(t, 0.0,1.0,colors='r',linestyles='dotted')
print('棄却域',t)
t = rvt.isf(0.995)
vlines(t, 0.0,1.0,colors='r',linestyles='dotted')
T = (sqrt(m+n-2)*(X-Y))/sqrt((1/m+1/n)*(m*Sx**2+n*Sy**2))
vlines(T, 0.0,1.0,colors='g',linestyles='dashed')
print('検定統計量',T)
title('Average Value:t-distribution')
show()



