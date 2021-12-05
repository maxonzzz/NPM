from scipy.integrate import odeint
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy import interpolate
s = np.array([25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]) #speed
t = np.linspace(0, 11, 12)
#speed and time output
print ( 'time = ', t)
print('speed = ', s)
plt.figure(figsize=(13, 8))
plt.subplot(2, 2, 1)
plt.plot(t, s, 'o-r', alpha=1, label="function", lw=5, mec='b', mew=2, ms=10)
plt.legend()
plt.grid(True)
plt.title("First function")
plt.xlabel("time")
plt.ylabel("speed")

plt.subplot(2, 2, 2)
xx = np.linspace(t.min(), t.max(), 10000)
yy = interp1d(t, s, kind="cubic")(xx) # interp cubic spline
plt.plot(xx, yy, "b-")
plt.legend()
plt.grid(True)
plt.title("Integration")
plt.xlabel("time")
plt.ylabel("speed")

plt.subplot(2, 2, 3)
xx = np.linspace(t.min(), t.max(), 10000)
y2 = interp1d(t, s, kind='quadratic')(xx) # interp quadratic spline
plt.plot(xx, y2, "g-")
plt.legend()
plt.grid(True)
plt.title("Integration by quadratic")
plt.xlabel("time")
plt.ylabel("speed")

plt.subplot(2, 2, 4)
xx = np.linspace(t.min(), t.max(), 10000)
vt = np.divide(s, t)
y3 = interp1d(t, vt, kind='quadratic')(xx) # interp quadratic spline
plt.plot(xx, y3, "r--")
plt.legend()
plt.grid(True)


plt.show()
