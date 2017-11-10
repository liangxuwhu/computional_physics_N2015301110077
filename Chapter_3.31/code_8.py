#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:28:27 2017

@author: lxwhu
"""

import numpy as np
import matplotlib.pyplot as plt
import math
def elliptical(a,b):
    tau=2*math.pi/10000
    x=[]
    y=[]
    theta=[]
    theta.append(0)
    for i in range(10000):
        x.append(a*math.cos(theta[-1]))
        y.append(b*math.sin(theta[-1]))
        theta.append(theta[-1]+tau)
    return x,y
def trajectory(x0,y0,vx0,vy0,a1,b1,tt):
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
        if ((x[-1]/a1)**2+(y[-1]/b1)**2)>1:
            d=math.sqrt((x[-1]/a1**2)**2+(y[-1]/b1**2)**2)
            d2=math.sqrt(x[-1]**2+y[-1]**2)
            rt=math.sqrt((x[-1]/(d2*a1))**2+(y[-1]/(b1*d2))**2)
            rr=1.0/rt
            d1=2*rr-d2
            x.append(x[-1]*d1/d2)
            y.append(y[-1]*d1/d2)
            cs=x[-1]/(a1**2*d)
            ss=y[-1]/(b1**2*d)
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
    return x,y
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
c,d=elliptical(2.0,3.0)
v,f=trajectory(0,0,1.0,-2.0,2.0,3.0,5000)
plt.title('elliptical stadium(50s')
plt.xlim(-2.0,2.0)
plt.ylim(-3.0,3.0)
plt.plot(c,d)
plt.plot(v,f)
plt.sca(ax2)
c,d=elliptical(2.0,3.0)
v,f=trajectory(0,0,1.0,-2.0,2.0,3.0,10000)
plt.title('elliptical stadium(100s')
plt.xlim(-2.0,2.0)
plt.ylim(-3.0,3.0)
plt.plot(c,d)
plt.plot(v,f)
plt.sca(ax3)
c,d=elliptical(2.0,3.0)
v,f=trajectory(0,0,1.0,-2.0,2.0,3.0,100000)
plt.title('elliptical stadium(1000s')
plt.xlim(-2.0,2.0)
plt.ylim(-3.0,3.0)
plt.plot(c,d)
plt.plot(v,f)
plt.sca(ax4)
c,d=elliptical(2.0,3.0)
v,f=trajectory(0,0,1.0,-2.0,2.0,3.0,200000)
plt.title('elliptical stadium(2000s')
plt.xlim(-2.0,2.0)
plt.ylim(-3.0,3.0)
plt.plot(c,d)
plt.plot(v,f)
plt.show()