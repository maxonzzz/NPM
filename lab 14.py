from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from numpy import *

x = [1.6, 1.7, 1.8, 1.9, 2.0, 2.1]
y = [4.6, 7.32, 12.92, 26.1, 53.53, 123.69]


# x = [ 1.8, 1.9, 2.0, 2.1, 2.2, 2.3]
# y = [ 2.6, 5.8, 8.93, 12.1, 17.0, 22.56]

spl = UnivariateSpline(x,y)


xs = linspace(1, 2.8, 2000)
plt.plot(x,y, 'ro', xs, spl(xs), 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()