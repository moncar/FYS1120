# coding: utf-8
from numpy import pi, zeros

R = 116e-3 / 2.0 # m
r = 8.6e-3 / 2.0 # m
N = 640
n = 100
k = 0.98e-6 # Wb
D = 10

A = pi * r**2 # m^2

mu_0 = 4 * pi * 10**(-7) # N/A^2

I = 4 # A
S_1 = 1300
S_2 = 200

H = lambda I: N * I / float(2 * pi * R)
B = lambda dS: k * D * abs(dS) / float(2 * n * A)

M = lambda B, H: B / mu_0 - H

with open('Oppgave3.1.txt', 'w') as f:
    f.write("M = %.3g \\text{ når } B = %.3g \\text{ T og } H = %.3g " % (M(B(S_2 - S_1), H(I)), B(S_2 - S_1), H(I)))

S_2 = 1100
S_1 = 500
M_temp = M(B(S_2 - S_1), H(I))
B_r = lambda M: mu_0 * M
with open('Oppgave3.2.txt', 'w') as f:
    f.write("\\text{Remanent } B_r = %.3g \\text{ T}" % (B_r(M_temp)))
