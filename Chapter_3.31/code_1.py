#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:01:00 2017

@author: lxwhu
"""

import math
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color):
        plt.plot(self.t,self.z,color,label='r=$%d$'%self.r)

'''A=Position(0)
A.calculate()
A.plot('orange')
B=Position(10)
B.calculate()
B.plot('g-')'''
C=Position(200)
C.calculate()
C.plot('b-')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.savefig('fihure_5.png')
plt.show()