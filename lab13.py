from scipy import integrate
import numpy as np
from numpy import *
def f(x):
    return (1/(math.sqrt(x + 2)))

v,err = integrate.quad(f, 0.5, 1.3)
print ('Check for the rectangle method: ', v)

def f1(x):
    return 1/math.sqrt(2*x^2+0.7)

def tr(f1, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f1(a) + f1(b))
    for i in range (1, n):
        sum += f1(a + i * h)
    return sum * h
print ('trapezoidal method: ', tr(f1,1.4 , 2, 20))
v,err = integrate.quad(f1, 1.4, 2)
print('Check for trapezoidal: ', v)            