import pylab as pl
import math
class cannon_shell_trajectory:
    def __init__(self, x=0, y=0,  g=9.8, initial_speed=700, time_step = 0.01, theta=45,
                   B=0.00004, density=1, a=0.0065, alpha=2.5, Tr=300, T=302, y_0=10000):
        self.x=[x]
        self.y=[y]
        self.dt=time_step
        self.angle=theta
        self.v_x=initial_speed*math.cos(math.radians(self.angle))
        self.v_y=initial_speed*math.sin(math.radians(self.angle))
        self.p=density
        self.v=initial_speed
        self.B=B
        self.a=a
        self.alpha=alpha
        self.y_0=y_0
        self.Tr=Tr
        self.T=T
        self.g=g
    def run(self):
        while(self.y[-1] >= 0):
            self.v_x = self.v_x-self.B*self.p*self.v*self.v_x*(self.T/self.Tr)**self.alpha*math.exp(-self.y[-1]/self.y_0)*self.dt
            self.x.append(self.x[-1] + self.v_x * self.dt)
            self.v_y = self.v_y-self.g * self.dt-self.B*self.p*self.v*self.v_y*(self.T/self.Tr)**self.alpha*math.exp(-self.y[-1]/self.y_0)*self.dt
            self.y.append(self.y[-1] + self.v_y * self.dt) 
    def show_results(self):
        pl.plot(self.x, self.y)
        pl.title('Trajectory of cannon shell')
        pl.xlabel('x($m$)')
        pl.ylabel('y($m$)')
        pl.show()        
a = cannon_shell_trajectory()
a.run()
a.show_results()