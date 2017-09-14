#!/usr/bin/env python3

import math
def g(x):
    return(1/math.sqrt(2*math.pi))*math.exp(-x**2/2)    
def add(x):
    return (x+1)
def interval(f,a,b,dx):
    list_interval=[]
    N=int((b-a)/dx)
    for i in range(N):
        list_interval.append(f(a+i*dx))
    return list_interval
print(interval(add,0,10,1))
    
#def integrate(i,dx):
