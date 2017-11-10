import numpy as np
import matplotlib.pyplot as plt
import math
def trajectory(x0,y0,vx0,vy0,r,tt):
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
        if (x[-1]**2+y[-1]**2)>r**2:
            d=math.sqrt(x[-1]**2+y[-1]**2)
            d2=math.sqrt(vx**2+vy**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append(y[-1]*d1/d)
            cs=x[-1]/d
            ss=y[-1]/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
    return x,y     
def circle(r1):
    x1=[]
    y1=[]
    theta=[]
    theta.append(0)
    tu=2*math.pi/10000
    for j in range(10000):
        x1.append(r1*math.cos(theta[-1]))
        y1.append(r1*math.sin(theta[-1]))
        theta.append(theta[-1]+tu)
    return x1,y1
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
a,b=trajectory(0.5,0.5,-0.2,-0.4,1.0,5000)
a1,b1=circle(1.0)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)
plt.title('circular stadium(50s)')
plt.sca(ax2)
a,b=trajectory(0.5,0.5,-0.2,-0.4,1.0,10000)
a1,b1=circle(1.0)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)
plt.title('circular stadium(100s)')
plt.sca(ax3)
a,b=trajectory(0.5,0.5,-0.2,-0.4,1.0,100000)
a1,b1=circle(1.0)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)
plt.title('circular stadium(1000s)')
plt.sca(ax4)
a,b=trajectory(0.5,0.5,-0.2,-0.4,1.0,200000)
a1,b1=circle(1.0)
plt.plot(a,b)
plt.plot(a1,b1)
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)
plt.title('circular billiard(2000s)')

plt.show()