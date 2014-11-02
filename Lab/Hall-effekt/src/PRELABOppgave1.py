# coding: utf-8
from numpy import polyfit, polyval, zeros, array
from matplotlib.pylab import plot, show, title, xlabel, ylabel,\
        legend, hold, savefig

"""
Klasse som les punkter frå ei fil, interpolerer med eit polynom og 
plottar resultatet mot einannan.
"""
class EvaluatePoints:

    """
    Konstruktør som tek imot ei fil med x- og y-verdiar.
    """
    def __init__(self, datapoints):
        self.datapoints = datapoints
        # Finn antal punkter i fila.
        with open(self.datapoints, 'r') as f:
            self.n = sum(1 for line in f)

    """
    Metode som les verdiane frå fila og lagrar dei i klassa.
    """
    def storeValues(self):
        self.points = zeros((2, self.n))
        with open(self.datapoints, 'r') as f:
            counter = 0
            for values in f:
                self.points[0, counter] = float(values.split()[0])
                self.points[1, counter] = float(values.split()[1])
                counter += 1

    """
    Metode som nyttar numpy-biblioteket til å interpolere punkta
    med eit polynom.
    """
    def interpolate(self, deg, evalPoint):
        # Lager eit polynom av grad 'deg' ut frå punkta.
        self.poly = polyfit(self.points[0, :], self.points[1, :], deg)
        self.evaluated = zeros(self.n)
        for i in range(self.n):
            self.evaluated[i] = polyval(self.poly, self.points[0, i])

    """
    Metode som plottar datapunkta og polynomet mot einannan.
    """
    def plotPoints(self, TITLE):
        plot(self.points[0, :], self.points[1, :], '.')
        hold('on')
        plot(self.points[0, :], self.evaluated, '-')
        hold('off')
        title(TITLE)
        xlabel('x [m]')
        ylabel('B [T]')
        legend(('datapunkter', 'polynomtilnærming',), loc=1)
        savefig('PRELAB3.png')
        show()
