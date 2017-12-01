# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import time
from math import *
c_vx=[]
c_vy=[]
c_x=[]
c_y=[]
c_r=[]
c_t=[]
def Calculate():
    c_x.append(Initial_x)
    c_y.append(Initial_y)
    c_vx.append(Initial_vx)
    c_vy.append(Initial_vy)
    c_t.append(0.0)
    for i in range(range_i):
        c_r.append((c_x[i]**2+c_y[i]**2)**0.5)
        c_vx.append(c_vx[i]-(4*(pi**2)*c_x[i])*dt/(c_r[i]**(beta+1)))
        c_vy.append(c_vy[i]-(4*(pi**2)*c_y[i])*dt/(c_r[i]**(beta+1)))
        c_x.append(c_x[i]+c_vx[i+1]*dt)
        c_y.append(c_y[i]+c_vy[i+1]*dt)
        c_t.append(i*dt)
    print ("Total steps",range_i)
    return 0
#初始值
Initial_vx=0*pi
Initial_vy=1.8*pi
Initial_x=1.0
Initial_y=0.0
beta=2.05
total_t=5.0
dt=0.0001
#寻找远日点
range_i=int(total_t/dt)
print ("beta =",beta)
Calculate()
max_r=[]
max_rx=[]
max_ry=[]
for i in range(1,range_i-1):
    if c_r[i]>c_r[i-1] and c_r[i]>c_r[i+1]:
        max_r.append(c_r[i])
        max_rx.append(c_x[i])
        max_ry.append(c_y[i])
        big_r=c_r[i]
#寻找近日点
range_i=int(total_t/dt)
Calculate()
min_r=[]
min_rx=[]
min_ry=[]
for i in range(1,range_i-1):
    if c_r[i]<c_r[i-1] and c_r[i]<c_r[i+1]:
        min_r.append(c_r[i])
        min_rx.append(c_x[i])
        min_ry.append(c_y[i])
        small_r=c_r[i]
#计算e的值
a=(big_r+small_r)*0.5
c=(big_r-small_r)*0.5
e=c/a
print ("e=",e)
# 计算角度
max_angle=[]
for i in range(len(max_r)):
    max_angle.append(atan(max_ry[i]/max_rx[i]))
print ("max angle",max_angle,"rad")
delta_angle=max_angle[2]-max_angle[1]
print ("delta angle",delta_angle,"rad")
strbeta=str(beta)
plt.figure(figsize=(10,10))
plt.xlim(-2.0,2.0)
plt.ylim(-2.0,2.0)
plt.xlabel("x(AU)")
plt.ylabel("y(AU)")
plt.text(0,1.8,"Beta="+strbeta)
plt.plot(max_rx,max_ry,'r*',label = "max")
plt.plot(min_rx,min_ry,'r+',label = "min")
plt.scatter(c_x,c_y,color = "black",label = "trajectory",s=0.01)
plt.scatter(0,0,s=100,color = "black",label = "sun")
plt.legend()
plt.show()