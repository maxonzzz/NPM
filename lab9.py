import matplotlib.pyplot as plt 

import numpy as np 

import math 

 

 

x= [0.101,0.106,0.111,0.116,0.121,0.126] 

y= [1.2618,1.2764,1.2912,1.3061,1.3213,1.3366] 

h = x[1] - x[0] 

 

def dy(y,j): 

  m1 = [] 

  for i in range(len(y)): 

     m1.append(y[i] - y[i-1]) 

  m1.pop(0) 

  if j == 1: 

    return m1 

  else: 

    j-=1 

    return dy(m1,j) 

 

   

xNew1 = 0.104

xNew2 = 0.124

q1 = (xNew1-x[0])/h 

q2 = (xNew2 - x[5])/h 

Fx1 = y[0] + q1*dy(y,1)[0] + ((q1*(q1-1))/math.factorial(2)) * dy(y,2)[0] + ((q1*(q1-1)*(q1-2))/math.factorial(3))*dy(y,3)[0] + ((q1*(q1-1)*(q1-2)*(q1-3))/math.factorial(4)) * dy(y,4)[0] + ((q1*(q1-1)*(q1-2)*(q1-3)*(q1-4))/math.factorial(5)) * dy(y,5)[0] 

Fx2 = y[5] + q2*dy(y,1)[4] + ((q2*(q2+1))/math.factorial(2) )*dy(y,2)[3] + ((q2*(q2+1)*(q2+2))/math.factorial(3))*dy(y,3)[2] + ((q2*(q2+1)*(q2+2)*(q2+3))/math.factorial(4))*dy(y,4)[1] + ((q2*(q2+1)*(q2+2)*(q2+3)*(q2+4))/math.factorial(5))*dy(y,5)[0] 

print('first interpolate ', Fx1) 

print('second interpolate ', Fx2) 

 

newX = [0.104, 0.124] 

newY = [Fx1,Fx2] 

 

plt.grid(True)  

plt.plot(x, y, 'b--' )   

plt.plot(newX, newY, 'ro') 

plt.plot(x, y, 'yo') 

plt.xlabel('x')  

plt.ylabel('y')  

plt.title('')  
plt.legend(['tabl ','Fx','  ' ], loc='lower right') 
 
plt.show()