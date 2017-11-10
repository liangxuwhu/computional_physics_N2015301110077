#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:42:01 2017

@author: lxwhu
"""

import pylab as pl
import numpy as np
class billiard_problem:
    def __init__(self, initial_x=0.1, initial_y=0.1, initial_vx=0.8, initial_vy=0.3, time_step=0.01 ):
        self.dt=time_step
        self.x=[initial_x]
        self.y=[initial_y]
        self.vx=[initial_vx]
        self.vy=[initial_vy]
        self.t=[0]
        self.a=0
    def run(self):
        for i in range(1,20000):
            self.x.append(self.x[i-1]+self.vx[i-1]*self.dt)
            self.y.append(self.y[i-1]+self.vy[i-1]*self.dt)
            self.vx.append(self.vx[i-1])
            self.vy.append(self.vy[i-1])
            if (np.sqrt( self.x[i]**2+(self.y[i]-self.a)**2 ) > 1.0 and self.y[i]>0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y-a)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1],self.a)
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1],self.a)
            self.t.append(self.t[i - 1] + self.dt)
            if (np.sqrt( self.x[i]**2+(self.y[i]+self.a)**2 ) > 1.0 and self.y[i]<0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y+a)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1],self.a)
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1],self.a)
            self.t.append(self.t[i-1]+self.dt)
        return self.x, self.y
    def correct(self,condition,x,y,vx,vy,a):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
    def reflect(self,x,y,vx,vy,a):
        if(y>0):            
           v = np.sqrt(vx**2+vy**2)
           cos1 = (vx*x+vy*(y-a))/v
           cos2 = (vx*(y-a)-vy*x)/v
           vt = -v*cos1
           vc = v*cos2 
           vx_n = vt*x+vc*(y-a)
           vy_n = vt*(y-a)-vc*x
        if(y<0):            
           v = np.sqrt(vx**2+vy**2)
           cos1 = (vx*x+vy*(y+a))/v
           cos2 = (vx*(y+a)-vy*x)/v
           vt = -v*cos1
           vc = v*cos2 
           vx_n = vt*x+vc*(y+a)
           vy_n = vt*(y+a)-vc*x
        return vx_n,vy_n 
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta <np.pi:
            x.append(np.cos(theta))
            y.append(self.a+np.sin(theta))
            theta+= 0.01
        theta=-np.pi
        while theta <0:
            x.append(np.cos(theta))
            y.append(-self.a+np.sin(theta))
            theta+= 0.01
        x.append(1)
        y.append(self.a)
        pl.plot(x,y)        
    def show_results(self):
        pl.plot( self.x,self.y)
        pl.title('Circular stadium-trajectory')
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.xlabel('$x$')
        pl.ylabel('$v_x$')
        pl.show()
a = billiard_problem()
a.run()
a.show_results()
a.plot_boundary()