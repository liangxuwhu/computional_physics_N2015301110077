import pylab as pl
import math
class baseball_trajectory:
    def __init__(self, x=0, y=0,  g=9.8, initial_speed=49, time_step = 0.01, theta=45,
                   B=0.00423, a=0.0065,):
        self.x=[x]
        self.y=[y]
        self.dt=time_step
        self.angle=theta
        self.v_x=initial_speed*math.cos(math.radians(self.angle))
        self.v_y=initial_speed*math.sin(math.radians(self.angle))
        self.v=initial_speed
        self.B=B
        self.a=a
        self.g=g
    def run(self):
        while(self.y[-1] >= 0):
            self.v_x = self.v_x-self.B*self.v*self.v_x*self.dt
            self.x.append(self.x[-1] + self.v_x * self.dt)
            self.v_y = self.v_y-self.g * self.dt-self.B*self.v*self.v_y*self.dt
            self.y.append(self.y[-1] + self.v_y * self.dt) 
    def show_results(self):
        pl.plot(self.x, self.y)
        pl.title('baseball_trajectory_no wind')
        pl.xlabel('x($m$)')
        pl.ylabel('y($m$)')
        pl.show()        
a = baseball_trajectory()
a.run()
a.show_results()