#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:47:42 2019

@author: yjb
"""

import numpy as np
import matplotlib.pyplot as plt

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

step = 2
eta = 0.95

xr = x + step*dlr/2
xl = x - step*dlr/2

f = function(x)
f_sum = np.array(f)
#loop
g = 100

for i in range(g):
    gra_l = (f - function(x-0.0001*dlr))/0.001
    gra_r = (f - function(x+0.0001*dlr ))/0.001
    avg_l = (f - function(x-step*dlr))/step
    avg_r = (f - function(x+step*dlr))/step
    f_xl = gra_l+avg_l
    f_xr = gra_r+avg_r
    if max(f_xl, f_xr) < 0:
        theta = np.random.random(n)-0.5*np.ones(n)
        dlr = theta/np.sqrt(np.sum(theta**2))
        xr = x + step*dlr/2
        xl = x - step*dlr/2
        f_sum = np.append(f_sum, f)
    else:
        if f_xl > f_xr:
            x-=step*dlr
            f = function(x)
            f_sum = np.append(f_sum, f)
            
        else:
            x+=step*dlr
            f = function(x)
            f_sum = np.append(f_sum, f)
        theta = np.random.random(n)-0.5*np.ones(n)
        dlr = theta/np.sqrt(np.sum(theta**2))
        xr = x + step*dlr/2
        xl = x - step*dlr/2
    step*=eta

plt.plot(f_sum)
print(x)
print(f)
"""

class BAS_value:
    def __init__(self, n, step, function):
        self.n = n
        self.x = np.random.random(self.n)*step**2
        self.func = function
        self.theta = np.random.random(n)-0.5*np.ones(self.n)
        self.dlr = self.theta/np.sqrt(np.sum(self.theta**2))
        self.step = step
        self.backup = step
        self.eta = 0.95
        self.xr = self.x + self.step*self.dlr/2
        self.xl = self.x - self.step*self.dlr/2
        
    def direction_update(self):
        self.theta = np.random.random(self.n)-0.5*np.ones(self.n)
        self.dlr = self.theta/np.sqrt(np.sum(self.theta**2))
        self.xr = self.x + self.step*self.dlr/2
        self.xl = self.x - self.step*self.dlr/2
        
    def fit(self, g):
        self.f = self.func(self.x)
        f_sum = np.array(self.f)
        for i in range(g):
            self.f_xl, self.f_xr = self.cal()
            
            if max(self.f_xl, self.f_xr) < 0:
                self.direction_update()
                f_sum = np.append(f_sum, self.f)
            
            else:
                if self.f_xl > self.f_xr:
                    self.x-=self.step*self.dlr
                    self.f = self.func(self.x)
                    f_sum = np.append(f_sum, self.f)
                else:
                    self.x+=self.step*self.dlr
                    self.f = self.func(self.x)
                    f_sum = np.append(f_sum, self.f)
                    
                self.direction_update()
                self.step*=self.eta
#        plt.plot(f_sum)
#        print(self.x)
#        print(self.f)
        return f_sum,self.f
                    
                    
    def cal(self):
        gra_l = (self.f - self.func(self.x-0.0001*self.dlr))/0.001
        gra_r = (self.f - self.func(self.x+0.0001*self.dlr ))/0.001
        avg_l = (self.f - self.func(self.x-self.step*self.dlr))/self.step
        avg_r = (self.f - self.func(self.x+self.step*self.dlr))/self.step
        f_xl = gra_l+avg_l
        f_xr = gra_r+avg_r
        return f_xl, f_xr
        #return f_xl, f_xr
        
    def x_init(self):
        self.x = np.random.random(self.n)*self.backup**2
        self.step = self.backup


class BAS_gra:
    def __init__(self, n, step, function):
        self.n = n
        self.x = np.random.random(self.n)*step**2
        self.func = function
        self.theta = np.random.random(n)-0.5*np.ones(self.n)
        self.dlr = self.theta/np.sqrt(np.sum(self.theta**2))
        self.step = step
        self.backup = step
        self.eta = 0.95
        self.xr = self.x + self.step*self.dlr/2
        self.xl = self.x - self.step*self.dlr/2
        
    def direction_update(self):
        self.theta = np.random.random(self.n)-0.5*np.ones(self.n)
        self.dlr = self.theta/np.sqrt(np.sum(self.theta**2))
        self.xr = self.x + self.step*self.dlr/2
        self.xl = self.x - self.step*self.dlr/2
        
    def fit(self, g):
        self.f = self.func(self.x)
        f_sum = np.array(self.f)
        for i in range(g):
            self.f_xl, self.f_xr = self.cal()
            
            if max(self.f_xl, self.f_xr) < 0:
                self.direction_update()
                f_sum = np.append(f_sum, self.f)
            
            else:
                if self.f_xl > self.f_xr:
                    self.x-=self.step*self.dlr
                    self.f = self.func(self.x)
                    f_sum = np.append(f_sum, self.f)
                else:
                    self.x+=self.step*self.dlr
                    self.f = self.func(self.x)
                    f_sum = np.append(f_sum, self.f)
                    
                self.direction_update()
            self.step*=self.eta
#        plt.plot(f_sum)
#        print(self.x)
#        print(self.f)
        return f_sum,self.f
                    
                    
    def cal(self):
        gra_l = (self.f - self.func(self.x-0.0001*self.dlr))/0.001
        gra_r = (self.f - self.func(self.x+0.0001*self.dlr ))/0.001
        avg_l = (self.f - self.func(self.x-self.step*self.dlr))/self.step
        avg_r = (self.f - self.func(self.x+self.step*self.dlr))/self.step
        f_xl = gra_l+avg_l
        f_xr = gra_r+avg_r
        return gra_l, gra_r
        #return f_xl, f_xr
        
    def x_init(self):
        self.x = np.random.random(self.n)*self.backup**2
        self.step = self.backup









