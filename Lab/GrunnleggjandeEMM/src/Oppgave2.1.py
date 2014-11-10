from numpy import array
from matplotlib.pylab import plot, show, xlabel, ylabel, title, legend

R = array([500, 700, 1000, 1200, 1500]) # Ohm
I = array([17.28, 12.45, 8.77, 7.33, 5.88])*10**(-3) # A
V = array([200.61, 144.56, 101.84, 85.07, 68.224])*10**(-3) # V

plot(I, V, 'o')
xlabel('I [A]')
ylabel('V [V]')
title('Inner resistance of an Amperemeter')
show()

dI = I[-1] - I[0]
dV = V[-1] - V[0]
R = dV/float(dI)
print ("Inner resistance of amperemeter: %g ohm" % R)
