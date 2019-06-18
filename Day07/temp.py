# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit

x = numpy.linspace(0, 10)
y = 2 * x + 2 *numpy.random.rand(50) - 1  # just to get scatter

def lin(x, m, b):
  return m * x + b

pars, _ = curve_fit(lin, x, y, p0=[1., 0.])

plt.scatter(x, y)
plt.plot(x, lin(x, *pars))
plt.show()
