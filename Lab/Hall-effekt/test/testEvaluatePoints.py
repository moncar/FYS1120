# coding: utf-8
import sys, os
sys.path.append(os.path.abspath('../src'))
from PRELABOppgave1 import EvaluatePoints
from unittest import TestCase, main
from numpy import linspace, zeros, polyval

class TestEvaluatePoints(TestCase):

    def setUp(self):
        self.deg = 3
        self.x = linspace(0, 5, 100)
        self.f = lambda t: t**2
        with open('testPoints.txt', 'w') as f:
            for i in range(100):
                f.write('%g \t %g \n' % (self.x[i], self.f(self.x[i])))

    def test_construction(self):
        self.EP = EvaluatePoints('testPoints.txt')
        self.assertEqual(self.EP.n, 100)

    def test_interpolation(self):
        self.EP = EvaluatePoints('testPoints.txt')
        self.EP.storeValues()
        self.EP.interpolate(2, 2)
        self.assertAlmostEqual(polyval(self.EP.poly, 0), self.f(0), places=5)
        self.assertAlmostEqual(polyval(self.EP.poly, 2), self.f(2), places=5)
    
    def test_plotPoints(self):
        self.EP = EvaluatePoints('testPoints.txt')
        self.EP.storeValues()
        self.EP.interpolate(2, 2)
        self.EP.plotPoints("TEST")
        

if __name__ == '__main__':
    main()
