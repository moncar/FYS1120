from Oppgave2 import ParticleInMagneticField
from numpy import array, cos, linalg, cross, zeros, linspace
from matplotlib.pylab import plot, show, title, legend, xlabel, ylabel, savefig

class Cyclotron(ParticleInMagneticField):

    def __init__(self, omega, E, B, m, q, r0, v0, t_start, t_final, dt):
        ParticleInMagneticField.__init__(self, E, B, m, q, r0, v0, t_start, t_final, dt)
        self.omega = omega

    def calculatePath(self):

        for i in range(self.n):
            if -0.1 <= self.r[i, 0] <= 0.1:
                F = q*(cross(self.v[i, :], self.B) + array([cos(self.omega*self.t[i]), 0, 0]))
            else:
                F = q*cross(self.v[i, :], self.B)

            a = F/float(self.m)
            self.v[i+1, :] = self.v[i, :] + a*self.dt
            self.r[i+1, :] = self.r[i, :] + self.v[i+1, :]*self.dt

    def escapeVelocity(self, rD):

        for i in range(self.n+1):
            if rD - linalg.norm(self.r[i, :]) <= 0:
                self.vesc = linalg.norm(self.v[i, :])
                finalTime = i
                break

        tempr = zeros(shape=(finalTime, 3))
        tempv = zeros(shape=(finalTime, 3))
        tempt = zeros(finalTime)
        
        for i in range(finalTime):
            tempr[i, :] = self.r[i, :]
            tempv[i, :] = self.v[i, :]
            tempt[i] = self.t[i]

        self.r = tempr
        self.v = tempv
        self.t = tempt
        print ("Escape velocity of proton: v = %g" % self.vesc)

    def plotCPath(self, TITLE):
        
        plot(self.r[:, 0], self.r[:, 1])
        title(TITLE)
        xlabel("x(t)")
        ylabel("y(t)")
        legend(("Proton",), loc=1)
#        savefig('3A.png')
        show()




if __name__ == '__main__':

    rD = 2.6
    m = 1
    q = 1
    v = array([0, 0, 0])
    r = array([0, 0, 0])
    tstart = 0
    tend = 50
    dt = 1.0e-3
    B = array([0, 0, 1])
    omega = q*linalg.norm(B)/float(m)
    E = array([0, 0, 0])

    cyclotron = Cyclotron(omega, E, B, m, q, r, v, tstart, tend, dt)
    cyclotron.calculatePath()
    cyclotron.plotCPath("Proton in cyclotron.")
    cyclotron.escapeVelocity(rD)
    cyclotron.plotPath("of proton in cyclotron.", 1)
