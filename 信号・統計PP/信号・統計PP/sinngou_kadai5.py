from numpy import *
from matplotlib.pyplot import *

Fs = 8000
f = 1000
k = 0
n = linspace(0,7,8)
y = cos((2.*pi*f*n)/Fs)
Re = fft.fft(y)
Im = fft.fft(imag(y))

subplot(2,1,1)
stem(n*1000,Re)
xlim([-500,7500])
subplot(2,1,2)
stem(n*1000,Im)
xlim([-500,7500])
xlabel('Frequency[Hz]')
show()