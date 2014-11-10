import os, sys
sys.path.append(os.path.abspath('../../Hall-effekt/src/'))
from PRELABOppgave1 import EvaluatePoints
from numpy import exp, log, array
from matplotlib.pylab import plot, show, xlabel, ylabel, title, savefig

U_list = array([8.9110, 7.0, 5.5, 4.35, 3.44, 2.70, 2.1, 1.65, 1.32, 1.05,\
                0.81, 0.65, 0.515, 0.410, 0.324, 0.256, 0.204, 0.161, 0.128])
t_list = array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220,\
                240, 260, 280, 300, 320, 340, 360])

with open('datapointsIRV.txt', 'w') as f:
    for i in range(U_list.size):
        f.write("%g \t %g\n" % (t_list[i], log(U_list[i])))

tau = -1.0/((log(U_list[-1]) - log(U_list[0]))/float(t_list[-1] - t_list[0]))

with open("InnerRV.txt", 'w') as f:
    f.write("Tau is equal to: %g s\\\\ \n" % tau)
    f.write("Inner resistance: %g ohm" % (tau/float(8.3e-6)))

EP = EvaluatePoints('datapointsIRV.txt')
EP.storeValues()
EP.interpolate(2, 0)
EP.plotPoints("Inner resistance of Voltmeter.", "InnerRV.png", "t [s]", "V [V]")
