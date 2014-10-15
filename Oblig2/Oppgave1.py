from numpy import zeros, linspace, sin, array, amin, amax
from matplotlib.pylab import plot, show, title, legend, xlabel, ylabel, xkcd, hold, figure, savefig
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Testytest
#xkcd()

class ParticleInElectricField:

    def __init__(self, E, m, q, r0, v0, t_start, t_final, dt):

        self.E = E
        self.m = m
        self.q = q
        self.r0= r0
        self.v0 = v0
        self.t_start = t_start
        self.t_final = t_final
        self.dt = dt

        # Creating arrays and timestep.
        self.n = int(self.t_final/float(self.dt))
        self.t = linspace(self.t_start, self.t_final, self.n+1)
        self.r = zeros(shape=(self.n+1, 3))
        self.r[0, :] = self.r0
        self.v = zeros(shape=(self.n+1, 3))
        self.v[0, :] = self.v0
        self.EXACT = zeros(shape=(self.n+1, 3))

    def calculatePath(self):

        # Implementing Euler-Cromer.
        for i in range(self.n):
            F = self.q*self.E
            a = F/float(self.m)
            self.v[i+1, :] = self.v[i, :] + a*self.dt
            self.r[i+1, :] = self.r[i, :] + self.v[i+1, :]*self.dt
            # Implementing exact formula for path.
            # This formula is found from analytical integration.
            self.EXACT[i+1, :] = 0.5*self.q/float(self.m)*self.E*self.t[i]**2

    def plotPath(self, TITLE, optn):

        if optn == 0:

            """
            Plotting the path in x-direction as a function of time.
            Showing the exact and the numerical representation in the same plot.
            """
            plot(self.t, self.r[:, 0])
            hold('on')
            plot(self.t, self.EXACT[:, 0])
            hold('off')
            title(TITLE)
            legend(('Approximation', 'Exact'), loc=2)
            xlabel("t in [0, 1]")
            ylabel("Position in x-direction")
#            savefig('A.png')
            show()

        elif optn == 1:

            """
            Plotting the path and the velocity of the particle.
            Showing all directions as a function of time.
            """
            figure()
            plot(self.t, self.r[:, 0])
            hold('on')
            plot(self.t, self.r[:, 1])
            plot(self.t, self.r[:, 2])
            hold('off')
            title("Positions " + TITLE)
            legend(('x(t)', 'y(t)', 'z(t)'), loc=2)
            xlabel("t in [0, 1]")
            ylabel("Positions for x, y and z-direction")
#            savefig('3A1.png')
            show()
            
            figure()
            plot(self.t, self.v[:, 0])
            hold('on')
            plot(self.t, self.v[:, 1])
            plot(self.t, self.v[:, 2])
            hold('off')
            title("Velocities " + TITLE)
            legend(('vx(t)', 'vy(t)', 'vz(t)'), loc=2)
            xlabel('t in [0, 1]')
            ylabel('Velocities in x, y and z-direction')
#            savefig('3A2.png')
            show()

        else:

            """
            Plotting the path of the particle in 3D.
            """
            # Something is funky here...
            fig = figure()
            ax = fig.add_subplot(1, 1, 1, projection='3d')
            ax.plot3D(self.r[:, 0], self.r[:, 1], self.r[:, 2], label='Position of particle')
            ax.legend(loc = 'lower left')
            ax.set_xlabel('Position in x-direction')
            ax.set_ylabel('Position in y-direction')
            ax.set_zlabel('Position in z-direction')
            ax.set_title(TITLE)
            ax.set_xlim(amin(self.r[:, 0]), amax(self.r[:, 0]))
            ax.set_ylim(amin(self.r[:, 1]), amax(self.r[:, 1]))
            ax.set_zlim(amin(self.r[:, 2]), amax(self.r[:, 2]))
#            savefig('2A4.png')
            show()


if __name__ == '__main__':

    # Assignment 1a) and 1b)
    E = array([5, 0, 0])
    r0 = array([0, 0, 0])
    v0 = array([0, 0, 0])
    dt = 1.0e-4
    t0 = 0
    tend = 1
    m = 2
    q = 3
    particle = ParticleInElectricField(E, m, q, r0, v0, t0, tend, dt)
    particle.calculatePath()
    particle.plotPath("Path of particle in constant electric field.", 0)

    # Assignment 1c) and 1d)
    E = array([1, 2, -5])
    particle = ParticleInElectricField(E, m, q, r0, v0, t0, tend, dt)
    particle.calculatePath()
    particle.plotPath("of particle in constant electric field.", 1)
    particle.plotPath("Position of particle in constant electric field.", 2)

