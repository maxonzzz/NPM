import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
x  = [-1, 0, 1, 2]
y  = [5, -11, -3, 23]

def Lagrange(x,y,k):
    summ =0
    for g in range (len (y)):
        p1=1
        p2=1
        for i in range (len(x)):
            if i == g:
                p1 *=1
                p2 *=1
            else:
                p1 *=(k-x[i])
                p2 *=(x[g]-x[i])
        summ += y[g]*p1/p2
    return summ
newX= np.linspace (min(x),max(x))
newY= [ Lagrange(x,y,i) for i in newX ]
plt.plot(x,y, 'o', newX, newY)
plt.xlabel('x') 
plt.ylabel('y')
plt.grid(axis='both')
plt.title('lb7')
plt.show()

f= lagrange(x,y)
fig=plt.figure(figsize=(10,8))
plt.plot(newX, f(newX), 'b',x,y,'ro')
plt.title('Lagrange')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()