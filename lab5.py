import numpy as np
import math


#перевірка
a = np.matrix([[1, 1, -1], [3, -1, 2], [4, 4, -3]])
b = np.matrix([[-2], [9], [-5]])



def gauss():
    n = len(b)
    for k in range (1, n):
        for i in range(k+1, n):
            if  a[i,k] != 0.0:
                a[i, k+1:n] = a[i, k+1: n] - a[i,k]/a[k,k]  * a[k,k+1:n]
                b[i] = b[i] - a[i,k]/ a[k,k] * b[k]

    for k in range( n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n])/a[k,k])        
    
    print('Проверка: \n', np.linalg.solve(a,b))
    print('Jordan - Gaus \n', np.linalg.inv(a) * b)
    return b


print(gauss(np.matrix([[1, 1, -1], [3, -1, 2], [4, 4, -3]]),np.matrix([[-2], [9], [-5]])))


