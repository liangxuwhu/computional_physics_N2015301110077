#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:21:29 2017

@author: lxwhu
"""

import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
class baseball_trajectory:
    def __init__(self, x=0, y=0, z=0, g=9.8, initial_speed=49, time_step = 0.01, theta=45,
                   B=0.00423, w=209.44, S=0.00041, a=0.0065,):
        self.x=[x]
        self.y=[y]
        self.z=[z]
        self.dt=time_step
        self.angle=theta
        self.v_x=initial_speed*math.cos(math.radians(self.angle))
        self.v_y=initial_speed*math.sin(math.radians(self.angle))
        self.v_z=0
        self.v=initial_speed
        self.S=S
        self.B=B
        self.w=w
        self.g=g
    def run(self):
        while(self.y[-1] >= 0):
            self.v_x = self.v_x-self.B*self.v*self.v_x*self.dt
            self.x.append(self.x[-1] + self.v_x * self.dt)
            self.v_y = self.v_y-self.g * self.dt
            self.y.append(self.y[-1] + self.v_y * self.dt)
            self.v_z = self.v_z-self.S*self.w*self.v_x*self.dt
            self.z.append(self.z[-1] + self.v_z * self.dt)
    def show_results(self):
        ax.plot(self.x, self.y, self.z)
        ax.set_title('A curve baseball trajectory')
        ax.set_zlabel('Z') #坐标轴
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        plt.show()        
a = baseball_trajectory()
a.run()
a.show_results()