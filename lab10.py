import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [0.6, 0.7, 1.0, 1.5, 1.9] 
y=  [2.64, 3.73, 1.42, 1.84, 0.65]
spl = UnivariateSpline(x, y)
xs = linspace(0, 7, 1000)
plt.plot(x,y, 'ro', xs, spl(xs), 'g')

plt.grid(color = 'r',
        linestyle = '-')
plt.xlabel('axis x')
plt.ylabel(' axis y')
plt.title('Spline interpolation')
plt.show()       