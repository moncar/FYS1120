from numpy import array, pi

g = 9.81 # m/s^2
mu_0 = 4 * pi * 10**(-7) # N/A^2
B = 0.75 # T
r1 = 11.04e-3 / 2.0 # m
r2 = 10.96e-3 / 2.0 # m
r3 = 10.27e-3 / 2.0 # m

R = (r1 + r2 + r3) / 3.0 # m (mean radius)
A = pi * R**2 # m^2
m1 = 40.61e-3 # kg
m2 = 40.335e-3 # kg

chi_func = lambda m: -2 * mu_0 / (A * B**2) * m * (-g)

with open('Oppgave1.txt', 'w') as f:
    f.write("\\chi = %.3g \\text{ T^{-1}}" % (chi_func(m2 - m1)))
