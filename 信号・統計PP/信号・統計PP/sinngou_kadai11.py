from matplotlib.pyplot import *
import cmath

plt = subplot(111,polar=True)
title('Location of polar')
a = cmath.polar(0.4-0.663j)
b = cmath.polar(0.4+0.663j)
print(a)
print(b)
plot(a[1],a[0],'x')
plot(b[1],b[0],'x')
ylim(0,1)
show()
