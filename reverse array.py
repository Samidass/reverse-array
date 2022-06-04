# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 08:18:23 2022

@author: Sammy
"""

import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    b=numpy.flip(a)
    return b
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

'''4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 '''