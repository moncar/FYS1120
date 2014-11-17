from numpy import array, sum as npsum

NA = 39.5e-3 # m^2
D = 10
k = 1.78e-6 # from last assignment
S = array([998, 945, 953, 989, 934, 995])

S_mean = npsum(S) / float(S.size)

B = k * D * S_mean / float(NA)

with open("Oppgave2.2.txt", 'w') as f:
    f.write("B = %.3g \\text{ T}" % B)
