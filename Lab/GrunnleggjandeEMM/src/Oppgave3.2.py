import os, sys
sys.path.append(os.path.abspath('../../Hall-effekt/src/'))
from PRELABOppgave1 import EvaluatePoints
from numpy import array
from matplotlib.pylab import plot, show, xlabel, ylabel, legend, title

R = array([1, 1.5, 2.5, 4, 10]) # Ohm
V = array([119.0, 137.6, 162.0, 181.4, 207.2])*10**(-3) # V

I_formula = lambda v, r: v/float(r)

I = []

for i in range(R.size):
    I.append(I_formula(V[i], R[i]))

I = array(I)

plot(I, V, 'o')
xlabel('I [A]')
ylabel('V [V]')
title('Inner resistance of Peltier-element')
show()

dI = I[-1] - I[0]
dV = V[-1] - V[0]
R_i = -dV/float(dI)
print ("Inner resistance of Peltier-element: %g ohm" % R_i)

with open('datapoints.txt', 'w') as f:
    for i in range(R.size):
        f.write("%g \t %g\n" % (I[i], V[i]))

EP = EvaluatePoints('datapoints.txt')
EP.storeValues()
EP.interpolate(2, 0)
EP.plotPoints("TEST")

ems = V[3] + R_i * I[3]
print ("EMS of Peltier-element: %g V" % ems)
