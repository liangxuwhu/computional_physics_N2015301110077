import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
class baseball_trajectory:
    def __init__(self, x=0, y=0, z=0, time_step = 0.00000000001, B=1, E=0, h=100000000, g=0):
        self.x=[x]
        self.y=[y]
        self.z=[z]
        self.dt=time_step
        self.v_x=17320000
        self.v_y=0
        self.v_z=15000000
        self.h=h
        self.B=B
        self.E=E
        self.g=g
    def run(self):
        while(self.z[-1] <= 5):
            self.v_x = self.v_x+self.B*self.h*self.v_y*self.dt
            self.x.append(self.x[-1] + self.v_x * self.dt)
            self.v_y = self.v_y+self.h * self.E * self.dt-self.B*self.h*self.v_x*self.dt
            self.y.append(self.y[-1] + self.v_y * self.dt)
            self.v_z = self.v_z-self.g*self.dt
            self.z.append(self.z[-1] + self.v_z * self.dt)
    def show_results(self):
        ax.plot(self.x, self.y, self.z)
        ax.set_title('Trajectory of the motion')
        ax.set_zlabel('Z') #坐标轴
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        plt.show()        
a = baseball_trajectory()
a.run()
a.show_results()