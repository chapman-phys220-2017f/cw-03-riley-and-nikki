#!/usr/bin/env python3

import math     ### Put a blank line after import statements for aethetics
def g(x):
    return(1/math.sqrt(2*math.pi))*math.exp(-x**2/2)    ### Put a blank line between function definitions. Also put a space after "return" for clarity
def add(x):
    return (x+1)
def interval(f,a,b,dx):
    list_interval=[]
    N=int((b-a)/dx)
    for i in range(N):
        list_interval.append(f(a+i*dx))
    return list_interval

def integrate(i,dx):
    """integrate (i:interval, dx:float) return:float"""  ### Good start, but definitely make more professional docstrings
    area = 0
    for fval in i:
        area += fval * dx     ### Note that this adds one too many rectangles, so over-estimates the area
    return area
    
    
    
    
if __name__ == "__main__":
    print(interval(add,0,10,1))
