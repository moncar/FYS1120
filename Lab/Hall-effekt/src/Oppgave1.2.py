# coding: utf-8
from numpy import array, sqrt

B = array([6e-3, 42e-3, 74e-3, 108e-3, 142e-3, 175e-3]) # T
V = array([1.4e-3, 6.14e-3, 11.47e-3, 16.7e-3, 22.0e-3, 27.24e-3]) # V
I = 24.055e-3 # A
L = 20.0e-3 # m
b = 10.0e-3 # m
d = 1.0e-3 # m
q = 1.6e-19 # C
RH = lambda vh, b: vh*d/float(I*b)
N = lambda r: 1.0/float(q*r)
RH_mean = 0
NH_mean = 0

rH = open("RH_utskrift.txt", 'w')
nH = open("N_utskrift.txt", 'w')
for i in range(1, 6):
    RH_mean += RH((V[i] - V[i-1]), (B[i] - B[i-1]))
    rH.write("%g mV & %g mT & %.4f Vm/(AT) \\\\ \n" % ((V[i] - V[i-1])*10**3,\
                                                 (B[i] - B[i-1])*10**3,\
                                                  RH((V[i] - V[i-1]),\
                                                 (B[i] - B[i-1]))))
    NH_mean += N(RH((V[i] - V[i-1]), (B[i] - B[i-1])))
    nH.write("%.4f Vm/(AT) & %g AT/(VmC) \\\\ \n" %(RH((V[i] - V[i-1]),\
                                                 (B[i] - B[i-1])),\
                                                  N(RH((V[i] - V[i-1]),\
                                                 (B[i] - B[i-1])))))
rH.close()
nH.close()

RH_mean = RH_mean/float(6)
NH_mean = NH_mean/float(6)
v_mean = I/float(NH_mean*q*d*b)
with open("v_mean_utskrift.txt", 'w') as v:
    v.write("%.2f \\text{ m/s}" % (v_mean))

V_measured = 1.0 # V
v_e = sqrt(2*q*V_measured/float(9.10e-31)) # m/s
with open("v_e_utskrift.txt", 'w') as v_m:
    v_m.write("%.2f \\text{ m/s}" % (v_e))

I = 24.8 # mA
B = array([8e-3, 33e-3, 56e-3, 81e-3, 101e-3, 121e-3]) # T
V = array([-2e-3, -5.34e-3, -6.84e-3, -12.4e-3, -15.84e-3, -18.67e-3]) # V
q = -q # C

RH_mean = 0
NH_mean = 0
RH = lambda vh, b: vh*d/float(I*b)
N = lambda r: 1.0/float(q*r)
rH = open("RH_utskrift2.txt", 'w')
nH = open("N_utskrift2.txt", 'w')
for i in range(1, 6):
    RH_mean += RH((V[i] - V[i-1]), (B[i] - B[i-1]))
    rH.write("%g mV & %g mT & %g Vm/(AT) \\\\ \n" % ((V[i] - V[i-1])*10**3,\
                                                 (B[i] - B[i-1])*10**3,\
                                                  RH((V[i] - V[i-1]),\
                                                 (B[i] - B[i-1]))))
    NH_mean += N(RH((V[i] - V[i-1]), (B[i] - B[i-1])))
    nH.write("%g Vm/(AT) & %g AT/(VmC) \\\\ \n" %(RH((V[i] - V[i-1]),\
                                                 (B[i] - B[i-1])),\
                                                  N(RH((V[i] - V[i-1]),\
                                                 (B[i] - B[i-1])))))
rH.close()
nH.close()

RH_mean = RH_mean/float(6)
NH_mean = NH_mean/float(6)
v_mean = I/float(NH_mean*q*d*b)
with open("v_mean_utskrift2.txt", 'w') as v:
    v.write("%.2f \\text{ m/s}" % (v_mean))


