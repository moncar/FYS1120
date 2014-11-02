# coding: utf-8
from PRELABOppgave1 import EvaluatePoints
from numpy import pi, sqrt, zeros

my_0 = (4*pi)*10**(-7) # vakuum permeabiliteten.
a = 0.02 # radius i meter.
t = 0.035 # høgde i meter.
I = 10.0 # Ampere, denne må kunne endrast.
A = 2*pi*a # Areal over sida til magneten i kvadratmeter.
V = pi*a**2*t # Volumet til sylinderen i kubikkmeter.
j = I*A/float(V) # Straumtetthet i Ampere per meter.
Bx = lambda h: my_0/2.0*j*((h + t)/sqrt((h + t)**2 + a**2) - h/sqrt(h**2 + a**2))

h = zeros(6) # Evalueringspunkter.
evaluated = zeros(6) # Verdi av Bx i h.
for i in range(6):
    h[i] = i
    evaluated[i] = Bx(h[i])

with open('Oppgave3.txt', 'w') as f:
    for i in range(6):
        f.write('%g \t %g \n' % (h[i], evaluated[i]))

EP = EvaluatePoints('Oppgave3.txt')
EP.storeValues()
EP.interpolate(2, 1)
EP.plotPoints('Test av PRELAB-kode')
