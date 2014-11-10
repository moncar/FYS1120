from numpy import exp, log, array
from matplotlib.pylab import plot, show, xlabel, ylabel, legend, title, hold

U_list = array([8.9110, 7.0, 5.5, 4.35, 3.44, 2.70, 2.1, 1.65, 1.32, 1.05,\
                0.81, 0.65, 0.515, 0.410, 0.324, 0.256, 0.204, 0.161, 0.128])
t_list = array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220,\
                240, 260, 280, 300, 320, 340, 360])


plot(t_list, log(U_list), 'o')
hold('on')
#plot(t_list, tau_list)
hold('off')
xlabel('t [s]')
ylabel('ln(U) and tau')
legend(("ln(U(t))", "calculated tau",), loc=1)
title("")
show()

tau = -1.0/((log(U_list[-1]) - log(U_list[0]))/float(t_list[-1] - t_list[0]))
print ("Tau is equal to: %g" % tau)
print ("Inner resistance: %g ohm" % (tau/float(8.3e-6)))
