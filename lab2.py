import math



def func(x):
    f = 9 * x **4 + 12*x**3 - 36 * x ** 2 - 2
    return f

def dfucn(x):
    return  36 * x** 3 + 36 * x ** 2 - 72 * x 

def d2func(x):
    return 108 * x ** 2 + 72 * x - 72 

#метод пол деления      
def method1 (a , b , eps):
    
    while math.fabs(b - a) > eps:
        if func(a) * func((a+b)/2) < 0 :

            b = (a+b)/2
        else :
            a = (a+b)/2
    x = (a + b) /2    
    print("method/2 = ", x) 
    return(x) 
    

    

method1(-7, 0, 0.001 )

#метод хорд
def method2(a, b, eps):
    if func(a) * d2func(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xy = xi - (xi - x0)/(func(xi) - func(x0)) * func(xi)

    while math.fabs(xy - xi) > eps:
        xk = xy
        xy = xi - (xi - x0)/(func(xi) - func(x0)) * func(xi)
        m = func(xk)
        print("func(xk) =", round(m, 7))
        break             

method2( -7, 0 , 0.0001)