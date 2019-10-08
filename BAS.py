#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:45:06 2019

@author: yjb
"""


import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return (1+(x[0]+x[1]+1)**2*(19-14*x[0]+3*x[0]**2-14*x[1]+6*x[0]*x[1]+3*x[1]**2))*(30+(2*x[0]-3*x[1])**2*(18-32*x[0]+12*x[0]**2+48*x[1]-36*x[0]*x[1]+27*x[1]**2))

"""
#dimension
n = 2
x = np.random.random(n)

theta = np.random.random(n)-0.5*np.ones(n)
dlr = theta/np.sqrt(np.sum(theta**2))
xr = x + dlr/2
xl = x - dlr/2
step = 2
eta = 0.95
f = function(x)
f_sum = np.array(f)
#loop
g = 100

for i in range(g):
    f_xl = function(xl)
    f_xr = function(xr)
    if f < min(f_xl, f_xr):
        theta = np.random.random(n)-0.5*np.ones(n)
        dlr = theta/np.sqrt(np.sum(theta**2))
        xr = x + dlr/2
        xl = x - dlr/2
        f_sum = np.append(f_sum, f)
    else:
        if f_xl < f_xr:
            x-=step*dlr
            f_sum = np.append(f_sum, f_xl)
            f = f_xl
        else:
            x+=step*dlr
            f_sum = np.append(f_sum, f_xr)
            f = f_xr
        theta = np.random.random(n)-0.5*np.ones(n)
        dlr = theta/np.sqrt(np.sum(theta**2))
        xr = x + dlr/2
        xl = x - dlr/2
    step*=eta

plt.plot(f_sum)
print(x)
print(f)
"""
class BAS:
    def __init__(self, n, step, func):
        self.n = n
        self.x = np.random.random(self.n)
        self.theta = np.random.random(self.n)-0.5*np.ones(self.n)
        self.dlr = self.theta/np.sqrt(np.sum(self.theta**2))
        self.xr = self.x + self.dlr/2
        self.xl = self.x - self.dlr/2
        self.step = step
        self.backup = step
        self.eta = 0.95
        self.func = func
        
    def direction_update(self):
        self.theta = np.random.random(self.n)-0.5*np.ones(self.n)
        self.dlr = self.theta/np.sqrt(np.sum(self.theta**2))
        self.xr = self.x + self.dlr/2
        self.xl = self.x - self.dlr/2
    
    def fit(self, g):
        self.step = self.backup
        
        self.f = self.func(self.x)
        f_sum = np.array(self.f)
        for i in range(1,g+1):
            if i%100 == 0:
                self.step=2
            self.f_xl = self.func(self.xl)
            self.f_xr = self.func(self.xr)
            
            if self.f <= min(self.f_xl, self.f_xr):
                f_sum = np.append(f_sum, self.f)
            else:
                if self.f_xl < self.f_xr:
                    self.x-=self.step*self.dlr
                    f_sum = np.append(f_sum, self.f_xl)
                    self.f = self.f_xl
                else:
                    self.x+=self.step*self.dlr
                    f_sum = np.append(f_sum, self.f_xr)
                    self.f = self.f_xr
            self.direction_update()
            self.step*=self.eta
        #print("x:  ", self.x)
        #print("value: ", self.f)
        #plt.plot(f_sum)
        return f_sum,self.f
    def x_init(self):
        self.x = np.random.random(self.n)











