#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:25:18 2017

@author: lxwhu
"""

import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(x0,y0,vx0,vy0,r,l,tt):
    x=[]
    y=[]
    x.append(x0)
    y.append(y0)
    vx=vx0
    vy=vy0
    tau=0.01
    for i in range(tt):
        x.append(x[-1]+vx*tau)
        y.append(y[-1]+vy*tau)
        if y[-1]>=l and (x[-1]**2+(y[-1]-l)**2)>r**2:
            d=math.sqrt(x[-1]**2+(y[-1]-l)**2)
            d2=math.sqrt(vx**2+vy**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append((y[-1]-l)*d1/d+l)
            cs=x[-1]/d
            ss=(y[-1]-l)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
        elif y[-1]<=-l and (x[-1]**2+(y[-1]+l)**2)>r**2:
            d=math.sqrt(x[-1]**2+(y[-1]+l)**2)
            d2=math.sqrt(vx**2+vy**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append((y[-1]+l)*d1/d-l)
            cs=x[-1]/d
            ss=(y[-1]+l)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
        elif -l<y[-1]<l and x[-1]>r:
           x[-1]=2*r-x[-1]
           vx=-vx
        elif -l<y[-1]<l and x[-1]<-r:
           x[-1]=-2*r-x[-1]
           vx=-vx           
    return x,y     
def circle(r1,l1):
    x1=[]
    y1=[]
    theta=[]
    theta.append(0)
    tu=math.pi/10000
    for j in range(10000):
        x1.append(r1*math.cos(theta[-1]))
        y1.append(r1*math.sin(theta[-1])+l1)
        theta.append(theta[-1]+tu)
    theta1=[]
    theta1.append(math.pi) 
    for k in range(10000):
        x1.append(r1*math.cos(theta1[-1]))
        y1.append(r1*math.sin(theta1[-1])-l1)
        theta1.append(theta1[-1]+tu)
    return x1,y1
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
a,b=trajectory(0,0,-0.2,-0.4,1.0,0.01,5000)
a1,b1=circle(1.0,0.01)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.01,1.01)
plt.title('circular billiard(50s)')
plt.sca(ax2)
a,b=trajectory(0,0,-0.2,-0.4,1.0,0.01,10000)
a1,b1=circle(1.0,0.01)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.01,1.01)
plt.title('circular billiard(100s)')
plt.sca(ax3)
a,b=trajectory(0,0,-0.2,-0.4,1.0,0.01,100000)
a1,b1=circle(1.0,0.01)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.01,1.01)
plt.title('circular billiard(1000s)')
plt.sca(ax4)
a,b=trajectory(0,0,-0.2,-0.4,1.0,0.01,200000)
a1,b1=circle(1.0,0.01)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.01,1.01)
plt.title('circular billiard(2000s)')

plt.show()