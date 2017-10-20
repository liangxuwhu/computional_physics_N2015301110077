#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:44:31 2017

@author: lxwhu
"""

import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)


t=[]
t.append(0)
dt=0.01
g=9.8
end_time = 1000
angle=[]

for i in range(4):
    a=(35+i*5)*math.pi/180
    angle.append(a)
    
x_1=[]
v_x=[]
y_1=[]
v_y=[]
z_1=[]
v_z=[]
x_1.append(0)
y_1.append(0)
z_1.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
v_z.append(0)
for i in range(int(end_time/dt)):
    m=x_1[i]+v_x[i]*dt
    x_1.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_1[i]+v_y[i]*dt	
    y_1.append(o)
    p=v_y[i]-g*dt
    v_y.append(p)
    q=z_1[i]+v_z[i]*dt
    z_1.append(q)
    r=v_z[i]-0.086*v_x[i]*dt
    v_z.append(r)
    if o <= 0 :
        break

x_2=[]
v_x=[]
y_2=[]
v_y=[]
z_2=[]
v_z=[]
x_2.append(0)
y_2.append(0)
z_2.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
v_z.append(0)
for i in range(int(end_time/dt)):
    m=x_2[i]+v_x[i]*dt
    x_2.append(m)
    n=v_x[i]-0.00423*49*v_y[i]*dt
    v_x.append(n)
    o=y_2[i]+v_y[i]*dt	
    y_2.append(o)
    p=v_y[i]-g*dt
    v_y.append(p)
    q=z_2[i]+v_z[i]*dt
    z_2.append(q)
    r=v_z[i]
    v_z.append(r)
    if o <= 0 :
        break

x_3=[]
v_x=[]
y_3=[]
v_y=[]
z_3=[]
v_z=[]
x_3.append(0)
y_3.append(0)
z_3.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
v_z.append(0)
for i in range(int(end_time/dt)):
    m=x_3[i]+v_x[i]*dt
    x_3.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt-0.086*v_y[i]*dt
    v_x.append(n)
    o=y_3[i]+v_y[i]*dt	
    y_3.append(o)
    p=v_y[i]-g*dt
    v_y.append(p)
    q=z_3[i]+v_z[i]*dt
    z_3.append(q)
    r=v_z[i]
    v_z.append(r)
    if o <= 0 :
        break



x_4=[]
v_x=[]
y_4=[]
v_y=[]
z_4=[]
v_z=[]
x_4.append(0)
y_4.append(0)
z_4.append(0)
v_x.append(49*math.cos(angle[0]))
v_y.append(49*math.sin(angle[0]))
v_z.append(0)
for i in range(int(end_time/dt)):
    m=x_4[i]+v_x[i]*dt
    x_4.append(m)
    n=v_x[i]-0.00423*49*v_x[i]*dt
    v_x.append(n)
    o=y_4[i]+v_y[i]*dt	
    y_4.append(o)
    p=v_y[i]-g*dt-0.086*v_z[i]*dt
    v_y.append(p)
    q=z_4[i]+v_z[i]*dt
    z_4.append(q)
    r=v_z[i]
    v_z.append(r)
    if o <= 0 :
        break



ax.plot(x_1,y_1,z_1,label="sidearm curve ball")
ax.plot(x_2,y_2,z_2,label="overhand curve")
ax.plot(x_3,y_3,z_3,label="fastball")
ax.plot(x_4,y_4,z_4,label="no spin")
ax.set_title('Baseball_trajectory_Different pitches')
ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')

ax.legend()
plt.show()
