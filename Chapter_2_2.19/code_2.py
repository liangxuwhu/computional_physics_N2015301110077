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
for i in range(6):
    a=(30+i*5)*math.pi/180
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
v_x.append(49*math.cos(angle[1]))
v_y.append(49*math.sin(angle[1]))
for i in range(int(end_time/dt)):
    m=x_2[i]+v_x[i]*dt
    x_2.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_2[i]+v_y[i]*dt	
    y_2.append(o)
    p=v_y[i]-g*dt-0.00423*49*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break

x_3=[]
v_x=[]
y_3=[]
v_y=[]
x_3.append(0)
y_3.append(0)
v_x.append(49*math.cos(angle[2]))
v_y.append(49*math.sin(angle[2]))
for i in range(int(end_time/dt)):
    m=x_3[i]+v_x[i]*dt
    x_3.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_3[i]+v_y[i]*dt	
    y_3.append(o)
    p=v_y[i]-g*dt-0.00423*49*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break
    
x_4=[]
v_x=[]
y_4=[]
v_y=[]
x_4.append(0)
y_4.append(0)
v_x.append(49*math.cos(angle[3]))
v_y.append(49*math.sin(angle[3]))
for i in range(int(end_time/dt)):
    m=x_4[i]+v_x[i]*dt
    x_4.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_4[i]+v_y[i]*dt	
    y_4.append(o)
    p=v_y[i]-g*dt-0.00423*49*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break

x_5=[]
v_x=[]
y_5=[]
v_y=[]
x_5.append(0)
y_5.append(0)
v_x.append(49*math.cos(angle[4]))
v_y.append(49*math.sin(angle[4]))
for i in range(int(end_time/dt)):
    m=x_5[i]+v_x[i]*dt
    x_5.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_5[i]+v_y[i]*dt	
    y_5.append(o)
    p=v_y[i]-g*dt-0.00423*49*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break

x_6=[]
v_x=[]
y_6=[]
v_y=[]
x_6.append(0)
y_6.append(0)
v_x.append(49*math.cos(angle[5]))
v_y.append(49*math.sin(angle[5]))
for i in range(int(end_time/dt)):
    m=x_6[i]+v_x[i]*dt
    x_6.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_6[i]+v_y[i]*dt	
    y_6.append(o)
    p=v_y[i]-g*dt-0.00423*49*v_y[i]*dt
    v_y.append(p)
    if o <= 0 :
        break

pl.figure(figsize=(10,6))
pl.plot(x_1,y_1,label="$30^\circ$")
pl.plot(x_2,y_2,label="$35^\circ$")
pl.plot(x_3,y_3,label="$40^\circ$")
pl.plot(x_4,y_4,label="$45^\circ$")
pl.plot(x_5,y_5,label="$50^\circ$")
pl.plot(x_6,y_6,label="$55^\circ$")
pl.title('baseball_trajectory_different angle')
pl.xlabel("x(m)")
pl.ylabel("y(m)")
pl.xlim(0,130)
pl.ylim(0,70)
pl.legend()
pl.show()