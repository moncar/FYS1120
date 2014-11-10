from numpy import array, sin, pi, sum as npsum

NA = 11.0 # m^2
t_list = array([4.37, 2.09, 1.36, 1.01, 7.41, 9.65, 0.66]) # s
ems_0 = array([0.6, 1.1, 1.5, 2.8, 0.4, 0.2, 3.0])*10**(-3) # V

with open('Oppgave5table.txt', 'w') as f:
    for i in range(t_list.size):
        f.write("%g & %g \\\\ \n" % (t_list[i], ems_0[i]))

B = lambda ems, t: t * ems/float(4 * NA)

B_list = []

for i in range(t_list.size):
    B_list.append(B(ems_0[i], t_list[i]))

B_list = array(B_list)
B_mean = npsum(B_list)/float(B_list.size)

with open('MeanValue.txt', 'w') as f:
    f.write("Mean value of B: %g T" % B_mean)
