
from matplotlib.pyplot import *
from numpy import *


FigSize = (6,4)
omega_c = 0.3
omega=arange(0.01,1.0,0.01)
H = 1/sqrt(1+(omega_c/omega)**2)
fig=figure(figsize=FigSize)
plot(omega, 20*log10(abs(H)))
ylim(-10,2)
grid(True)
title('High-Pass Filter')
xlabel('Normalized Frequency')
ylabel('Gain [dB]') 
show()