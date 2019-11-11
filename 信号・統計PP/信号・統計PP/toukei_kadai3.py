# 例題3-3
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
# データ
S2 = 4.0
n = 7
m = 4 
alpha = 0.01

# グラフ
gxmin,gxmax = (0.01, 25)
gymin,gymax = (0.0, 0.7)

# 確率密度関数
t = np.arange(gxmin,gxmax,0.01)
rv = st.f(dfn=m-1,dfd=n-1)
f = rv.pdf(t)
#　確率変数値
t1 = rv.isf(alpha)
print('t1=',t1)
# 分散
T = ((m*(n-1))/(n*(m-1)))*10
print('T=',T)

fig = plt.figure(figsize=(6,4))
plt.plot(t,f)
plt.autoscale(tight=True)
plt.xlabel('z')
plt.ylabel('f(z)')
plt.vlines(t1,gymin,gymax,linestyles='--',colors='r')
plt.vlines(T,gymin,gymax,linestyles='--',colors='g')
plt.show()
