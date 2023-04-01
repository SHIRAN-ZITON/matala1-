# -*- coding: utf-8 -*-
"""
@author: shiran.ziton
"""

def my_func(x1,x2,x3):
    if x1+x2+x3 == 0:
        print("Not a number – denominator equals zero")
    elif type(x1) == int or type(x2) == int or type(x3) == int :
        print("“Error: parameters should be float”")
    elif type(x1) != float or type(x2) != float or type(x3) != float :
        print("nan")
    else:
        x = (x1+x2+x3)*(x2+x3)*x3/(x1+x2+x3)
        print(x)
    
my_func(4.0,2.0,6.0)