from numpy import array

I = array([1.0, 1.25, 1.5, 1.75, 1.99]) # A
I_A4 = array([1.012, 1.2614, 1.511, 1.762, 1.9975]) # A
I_A2 = array([1.006, 1.257, 1.507, 1.755, 2.001]) # A
V_A4 = array([0.058, 0.071, 0.085, 0.099, 0.112])*10**(-3) # V
V_A2 = array([3.926, 4.85, 5.78, 6.71, 7.642])*10**(-3) # V
I_C4 = array([1.008, 1.255, 1.5125, 1.76, 2.002]) # A
V_C4 = array([0.033, 0.04, 0.048, 0.055, 0.063])*10**(-3) # V
I_C2 = array([1.007, 1.253, 1.511, 1.761, 2.004]) # A
V_C2 = array([2.1, 2.5, 2.97, 3.41, 3.84])*10**(-3) # V

R_A4 = []
R_A2 = []
R_C4 = []
R_C2 = []

for i in range(I_A4.size):
    R_A4.append(V_A4[i]/float(I_A4[i]))
    R_A2.append(V_A2[i]/float(I_A2[i]))
    R_C4.append(V_C4[i]/float(I_C4[i]))
    R_C2.append(V_C2[i]/float(I_C2[i]))


with open('Oppgave4A.txt', 'w') as f:
    for i in range(I_A4.size):
        f.write("%g & %g & %g & %g & %g & %g\\\\ \n" % (R_A4[i], I_A4[i], V_A4[i],\
                                                        R_A2[i], I_A2[i], V_A2[i]))


with open('Oppgave4C.txt', 'w') as f:
    for i in range(I_A4.size):
        f.write("%g & %g & %g & %g & %g & %g\\\\ \n" % (R_C4[i], I_C4[i], V_C4[i],\
                                                        R_C2[i], I_C2[i], V_C2[i]))
