# coding: utf-8
from numpy import polyfit, polyval, zeros, array
from matplotlib.pylab import plot, show, title, xlabel, ylabel, legend, hold

class EvaluatePoints:

    def __init__(self, datapoints):
        self.datapoints = datapoints
        with open(self.datapoints, 'r') as f:
            self.n = sum(1 for line in f)

    def storeValues(self):
        self.points = zeros((2, self.n))
        with open(self.datapoints, 'r') as f:
            counter = 0
            for values in f:
                self.points[0, counter] = float(values.split()[0])
                self.points[1, counter] = float(values.split()[1])
                counter += 1

    def interpolate(self, deg, evalPoint):
        # Lager eit polynom av grad 'deg' ut frå punkta.
        self.poly = polyfit(self.points[0, :], self.points[1, :], deg)
        self.evaluated = zeros(self.n)
        for i in range(self.n):
            self.evaluated[i] = polyval(self.poly, self.points[0, i])

    def plotPoints(self, TITLE):
        plot(self.points[0, :], self.points[1, :], '.')
        hold('on')
        plot(self.points[0, :], self.evaluated, '-')
        hold('off')
        title(TITLE)
        xlabel('x punkter')
        ylabel('y punkter')
        legend(('datapunkter', 'polynomtilnærming',), loc=1)
        show()
