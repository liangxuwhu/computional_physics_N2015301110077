#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:49:06 2017

@author: lxwhu
"""

import pylab as pl
import math
class pendulum:
    def __init__(self, initial_theta=0.2,  initial_time=0, w=0):
        self.l=9.8       
        self.theta=[initial_theta]
        self.dt=0.01
        self.t=[initial_time]
        self.w=[w]
        self.g=9.8
        self.q=0.5
        self.f=1.35
        self.omiga=2/3
    def run(self):
        for i in range(10000): 
            self.w.append(self.w[i]-((self.g/self.l)*math.sin(self.theta[i])+self.q*self.w[i]-self.f*math.sin(self.omiga*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.w[i + 1]*self.dt)
            if self.theta[i+1] > math.pi:
                self.theta[i+1] = self.theta[i+1] -2 * math.pi
            elif self.theta[i+1] < -math.pi:
                    self.theta[i+1] = self.theta[i+1] +2 * math.pi
            else:
                pass
            self.t.append(self.t[i]+self.dt)
    def show_results(self):
        pl.plot(self.t,  self.theta)
        pl.title('$\Theta$ versue time')
        pl.xlabel('time($s$)')
        pl.ylabel('$\Theta$($radians$)')
        pl.show()
a = pendulum()
a.run()
a.show_results()