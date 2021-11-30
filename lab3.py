import math

def func(x):
    return 3 * x **4 - x ** 3 + 10 * x ** 2 - 5 * x - 3
    
def derivate(x):
    return 12 * x ** 3 - 3 * x ** 2 + 20 * x - 5

def derivate_2(x):
    return 36 * x ** 2 - 6 * x + 20

def NewTon(a , b , eps ):

    if func(b) * derivate_2(b) > 0:
        x = b
    else:
        x = a
    h = func(x)/ derivate(x)
    x = x - h
    if math.fabs(h) <= eps:
        print(x)
    else:
        h = func(x)/ derivate(x)
        x = x - h
    print("Neaton Method = " , x)    
            
    

NewTon( 0.25, 1, 0.001)





def combine(a, b, eps):
    if  derivate(a) * derivate_2(a) < 0:
        a0 = b
        b0 = a
    else:
        a0 = a
        b0 = b 

    xp1 = a0 
    xp2 = b0


    xn1 = xp1 - func(xp1)*(xp2-xp1)/(func(xp2) - func(xp1))
    xn2 = xp2 - func(xp2)/ derivate(xp2)
    xr1 = xn1
    xr2 = xn2

    while xr2 - xr1 > eps:
        x = (xr1 + xr2) / 2
        break    
        
            
    else:
        xn1 = xp1 - func(xp1)*(xp2-xp1)/(func(xp2) - func(xp1))
        xn2 = xp2 - func(xp2)/ derivate(xp2)
        xr1 = xn1
        xr2 = xn2
    print("Comb method = ", x)    
    

combine( 0.25, 1, 0.00001)






     
    

