from Oppgave1 import ParticleInElectricField
from numpy import linalg, cross, array, sin, cos

"""
Subclass of ParticleInElectricField.
The class makes use of some of the methods made in ParticleInElectricField.
"""
class ParticleInMagneticField(ParticleInElectricField):

    """
    Constructor storing most of the values in superclass.
    """
    def __init__(self, E, B, m, q, r0, v0, t_start, t_final, dt):

        ParticleInElectricField.__init__(self,\
                E, m, q, r0, v0, t_start, t_final, dt)
        self.B = B # Magnetic Field.

    """
    Method overriding ParticleInElectricFiled.calculatePath().
    """
    def calculatePath(self):

        for i in range(self.n):
            F = self.q*cross(self.v[i, :], self.B)
            a = F/float(self.m)
            self.v[i+1, :] = self.v[i, :] + a*dt
            self.r[i+1, :] = self.r[i, :] + self.v[i+1, :]*dt

    """
    Method calculating time used for a particle to make one complete revolution.
    """
    def calculateRevolutionTime(self):

        for i in range(1, self.n):
            # From the first graph we see that x(t) oscillates between positive
            # and negative values. We want to find the point where the function
            # changes from negative to positive values.
            if self.r[i, 0] <= 0 <= self.r[i+1, 0]:
                T = self.t[i+1]
                break

        print ("Time spent on one revolution: T = %g" % T)



if __name__ == '__main__':

    # Assignment 2a) and 2b)
    B = array([0, 0, 3])
    m = 2
    q = 3
    r0 = array([0, 0, 0])
    v0 = array([5, 0, 0])
    t0 = 0
    tend = 5
    dt = 1.0e-4
    particle = ParticleInMagneticField(0, B, m, q, r0, v0, t0, tend, dt)
    particle.calculatePath()
    particle.calculateRevolutionTime()
    particle.plotPath("Path of particle in constant magnetic field.", 1)
    particle.plotPath("Path of particle in constant magnetic field.", 2)

    # Assignment 2d)
    v0 = array([5, 0, 2])
    particle = ParticleInMagneticField(0, B, m, q, r0, v0, t0, tend, dt)
    particle.calculatePath()
    particle.plotPath("Path of particle in constant magnetic field.", 2)
