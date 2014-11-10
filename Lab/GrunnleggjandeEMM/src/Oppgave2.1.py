import sys, os
sys.path.append(os.path.abspath('../../Hall-effekt/src/'))
from PRELABOppgave1 import EvaluatePoints
from numpy import array
from matplotlib.pylab import plot, show, xlabel, ylabel, title, savefig

R = array([500, 700, 1000, 1200, 1500]) # Ohm
I = array([17.28, 12.45, 8.77, 7.33, 5.88])*10**(-3) # A
V = array([200.61, 144.56, 101.84, 85.07, 68.224])*10**(-3) # V

with open('Oppgave2.1table.txt', 'w') as f:
    for i in range(R.size):
        f.write("%g & %g & %g \\\\ \n" % (R[i], I[i], V[i]))

with open('Oppgave2.1datapoints.txt', 'w') as f:
    for i in range(R.size):
        f.write("%g \t %g \n" % (I[i], V[i]))

EP = EvaluatePoints('Oppgave2.1datapoints.txt')
EP.storeValues()
EP.interpolate(2, 0)
EP.plotPoints("Inner resistance of an Amperemeter", "InnerRA.png", "I [A]", "V [V]")

dI = I[-1] - I[0]
dV = V[-1] - V[0]
R = dV/float(dI)

with open('InnerRA.txt', 'w') as f:
    f.write("Inner resistance of amperemeter: %g ohm" % R)
