import numpy as np
N = 53 # カードの総数
pxy = np.zeros((2,2)) # 同時確率
for x in range(2): #：x=0 ダイヤではない、x=1：ダイヤである
    for y in range(2): # y=0: 絵札ではない、y=1：絵札である
        if x==0 and y==0:
            n = N - (12 + 13 - 3)
        elif x==0 and y==1:
            n = 9
        elif x==1 and y==0:
            n = 10
        elif x==1 and y==1:
            n = 3
        pxy[x,y] = n/N
px = np.zeros(2) # Xの周辺確率
for x in range(2):
    px[x] = np.sum(pxy[x,:])

py = np.zeros(2) # Yの周辺確率
for y in range(2):
    py[y] = np.sum(pxy[:,y])
for x in range(2):
    for y in range(2):
        print( '(x,y)=', x, y, (' 同時確率=%5.4f' % pxy[x,y]), ' 周辺確率の積=%5.4f' % (px[x]*py[y])) 
