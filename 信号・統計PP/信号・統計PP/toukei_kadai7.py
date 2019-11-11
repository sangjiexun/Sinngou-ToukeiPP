from numpy import *
from matplotlib.pyplot import *
# データの読み込み
file = 'Data/TestScore.csv'
data = loadtxt(file,delimiter=',')
#print(data[1,:])
x = data[0,:] # 中間
y = data[1,:] # 期末
# 統計量
xBar = mean(x) 
yBar = mean(y)
Sx2 = var(x,ddof=0) 
Sy2 = var(y,ddof=0) 
C = cov(x,y,ddof=0)
Sxy = C[0,1]
# 回帰係数
a = Sxy/Sx2
b = yBar - a*xBar
r = Sxy/(sqrt(Sx2)*sqrt(Sy2))
print('a=',a,'  b=',b,' r=',r)
# グラフ
scatter(x,y)
xlabel('Chukan')
ylabel('Kimatu')
autoscale(enable=True,axis='x',tight=True)
gx = linspace(30,100,100)
gy = a*gx + b
plot(gx,gy,'r--')
str = f"y={a:.2f}x + {b:.2f}\nr = {r:.2f}"
text(35,80,str)
legend()
grid()
show()
