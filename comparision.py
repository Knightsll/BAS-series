#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:12:10 2019

@author: yjb
"""

import numpy as np
import matplotlib.pyplot as plt
from BAS import BAS
from BAS_value import BAS_value,BAS_gra

def function(x):
    return (1+(x[0]+x[1]+1)**2*(19-14*x[0]+3*x[0]**2-14*x[1]+6*x[0]*x[1]+3*x[1]**2))*(30+(2*x[0]-3*x[1])**2*(18-32*x[0]+12*x[0]**2+48*x[1]-36*x[0]*x[1]+27*x[1]**2))

#Easom function
def function2(x):
    return -np.cos(x[0])*np.cos(x[1])*np.exp(-(x[0]-np.pi)**2-(x[1]-np.pi)**2)

#sum squares function
def function3(x):
    return np.sum(np.array([(i+1)*x[i]**2 for i in range(len(x))]))

def function4(x):
    return np.sum(np.array([np.sin(x[i])*(np.sin(i*x[i]**2/np.pi))**20 for i in range(len(x))]))

#eggholder
def function5(x):
    return -(x[1]+47)*np.sin(np.sqrt(np.abs(x[1]+x[0]/2.+47)))-x[0]*np.sin(np.sqrt(np.abs(x[0]-(x[1]+47))))

#schaffer
def function6(x):
    return 0.5+ (np.cos(np.sin(np.abs(x[0]**2-x[1]**2)))-0.5)/(1+0.001*(x[0]**2+x[1]**2))**2

def function7(x):
    return np.sum(np.array([x[i]**4-16*x[i]**2+5*x[i] for i in range(len(x))]))/2

x = [i for i in range(101)]

#Modify diamension step and function here
bas = BAS(100, np.sqrt(5), function4)
bas_improve = BAS_value(100, np.sqrt(5), function4)
bas_gra = BAS_gra(100, np.sqrt(5),function4)



y_bas = bas.fit(100)[0]
y_bas_improve = bas_improve.fit(100)[0]
y_bas_gra = bas_gra.fit(100)[0]

plt.figure(figsize = (10,5))

plt.subplot(1,2,1)
plt.title("Convergence rate above three algorithms")
plt.plot(x, y_bas,'r-', label = 'BAS')
plt.plot(x, y_bas_improve,'g-', label = 'BAS_value')
plt.plot(x, y_bas_gra, 'b-', label = 'BAS_gra')
plt.legend(loc = 'best')
plt.xlabel('Iterations')
plt.ylabel('f')
print("y_values: ",y_bas[-1], y_bas_gra[-1], y_bas_improve[-1])


y_bas = np.array([])
y_bas_improve = np.array([])
y_bas_gra = np.array([])

for i in range(100):
    y_bas = np.append(y_bas, bas.fit(100)[1])
    y_bas_improve = np.append(y_bas_improve, bas_improve.fit(100)[1])
    y_bas_gra = np.append(y_bas_gra, bas_gra.fit(100)[1])
    bas.x_init()
    bas_improve.x_init()
    bas_gra.x_init()

plt.subplot(1,2,2)
plt.title("Results executed 100 times algorithm")
plt.plot(x[:100], y_bas,'r-', label = 'BAS')
plt.plot(x[:100], y_bas_improve,'g-', label = "BAS_value")
plt.plot(x[:100], y_bas_gra,'b-', label = "BAS_gra")
plt.xlabel('Times')
plt.ylabel('Best results')
plt.legend(loc = "best")
print("y_means:   ",y_bas.mean(), y_bas_gra.mean(), y_bas_improve.mean())
print("y_std:     ",y_bas.std(), y_bas_gra.std(), y_bas_improve.std())





