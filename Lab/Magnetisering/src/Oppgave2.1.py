S = 2000
V0 = 0.866e-3 # V
t0 = 41.09 # s
D = 10

k = V0 * t0 / float(D * S)

with open('Oppgave2.1.txt', 'w') as f:
    f.write("k = %.3g" % k)
