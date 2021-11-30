import math
import numpy as np

y = np.array([3.526, 3.782, 3.945, 4.043, 4.104, 4.155])
x = np.array([2.4, 2.6, 2.8, 3.0, 3.2, 3.4])
h = x[1]-x[0]
def dy(y,j):
    m1=[]
    for i in range(len(y)):
        m1.append(y[i]-y[i-1]) 
    m1.pop(0)
    if j ==1:
        return m1
    else:
        j-=1          
        return dy(m1,j) 
yx1=1/h*dy(y,1)[1]-dy(y, 2)[1]/2+dy(y, 3)[1]/3-dy(y, 4)[1]/4

print ( "1derivative =" , yx1)
yx2=1/h**2*dy(y, 2)[1]-dy(y, 3)[1]+11/12*dy(y,4)[1]

print ( "2derivative =" , yx2)