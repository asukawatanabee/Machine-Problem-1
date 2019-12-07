#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:16:39 2019

@author: asukawatanabe
"""

import matplotlib.pyplot as plt
def f(n):
    if n <= 9:
        return n*n-7
    return f(n-10)

if __name__ == '__main__' :
    x = []
    y = []
    for i in range(1,100):
        x.append(i)
        y.append(f(i))
        
        print(x)
        print(y)
        plt.plot(x,y)
        
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        
        plt.title( 'The graph for f(n)' )
       
        plt.show()