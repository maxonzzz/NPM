import math
import numpy as np
import copy
import itertools

from scipy.optimize.slsqp import fun
def funcs(n,x):
    if  n ==1:
        return   math.cos(x[1]-1) + x[0] - 0.5 
    elif n== 2:
        return x[1] - math.cos(x[0])-3
    
def method(n,m,x,eps = 1e-3):
    k = 0
    while True:
        d = 0, b = copy.deepcopy(x); a =copy.deepcopy(b)
        a[1] = funcs(1,x)
        x[1] = a [1]
        a[2] = funcs(2,x)
        x[2] = a[2]
        a = copy.deepcopy(b)
        for i in range(1, n+1):
            d1 = abs(x[i]- a[i])
            if d <d1:
                d = d1
                k +=1
                if d <= eps:
                    print("sol",x, "Iter = " , k)
                    break
                else:
                    a = copy.deepcopy(x)
    if k>m:
        print("Error")
        exit(0)

method(2,10 np.array([]))

