import matplotlib.pyplot as plt

from numpy import *
import sympy as sp

from math import *

def taylor(x):
    y = 0
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    d4 = sp.diff(d3, x)
    print('d1 = ', d1)
    print('d2 = ', d2)
    print('d3 = ', d3)
    print('d4 = ', d4)
    x = 0
    d01 = -2*sin(sin(2*x))*cos(2*x)
    d02 = 4*sin(2*x)*sin(sin(2*x)) - 4*cos(2*x)**2*cos(sin(2*x))
    d03 = 24*sin(2*x)*cos(2*x)*cos(sin(2*x)) + 8*sin(sin(2*x))*cos(2*x)**3 + 8*sin(sin(2*x))*cos(2*x)
    f0 = sp.cos(sp.sin(2*x))
    print('d01 = ' ,d01)
    print('d02 = ' ,d02)
    print('d03 = ' ,d03)
    
    y = f0 + d01*t + d02 *(t-0) ** 2/2 + d03*(t-0) ** 3/6
    print ('y= ', y)
    return y

x = sp.symbols('x')
t = sp.symbols('t')
f = sp.cos(sp.sin(2*x))
taylorr = taylor(x)

# pl = sp.plot(f, taylorr, (x, -5, 5), label= 'Taylor')
# pl.show()