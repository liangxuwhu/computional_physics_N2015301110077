#!/usr/bin/env pytho`n2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:26:38 2017

@author: lxwhu
"""

import math
import numpy as np
import matplotlib.pyplot as pl

t=[]
t.append(0)
dt=0.01
g=9.8
end_time = 1000
angle=[]
for i in range(3):
    a=(35+i*5)*math.pi/180
    angle.append(a)

x_1=[]
v_x=[]
y_1=[]
v_y=[]
x_1.append(0)
y_1.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
for i in range(int(end_time/dt)):
    m=x_1[i]+v_x[i]*dt
    x_1.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_1[i]+v_y[i]*dt	
    y_1.append(o)
    p=v_y[i]-g*dt-0.00423*49*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break


x_2=[]
v_x=[]
y_2=[]
v_y=[]
x_2.append(0)
y_2.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
for i in range(int(end_time/dt)):
    m=x_2[i]+v_x[i]*dt
    x_2.append(m)
    n=v_x[i]-0.00423*45*v_x[i]*dt
    v_x.append(n)
    o=y_2[i]+v_y[i]*dt	
    y_2.append(o)
    p=v_y[i]-g*dt-0.00423*45*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break

x_3=[]
v_x=[]
y_3=[]
v_y=[]
x_3.append(0)
y_3.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
for i in range(int(end_time/dt)):
    m=x_3[i]+v_x[i]*dt
    x_3.append(m)
    n=v_x[i]-0.00423*53*v_x[i]*dt
    v_x.append(n)
    o=y_3[i]+v_y[i]*dt	
    y_3.append(o)
    p=v_y[i]-g*dt-0.00423*53*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break
    


pl.figure(figsize=(10,6))
pl.plot(x_1,y_1,label="no wind")
pl.plot(x_2,y_2,label="tail wind")
pl.plot(x_3,y_3,label="$head wind$")
pl.title('Baseball_trajectory_Different Wind')
pl.xlabel("x(m)")
pl.ylabel("y(m)")
pl.xlim(0,130)
pl.ylim(0,40)
pl.legend()
pl.show()
