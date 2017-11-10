import pylab as pl
class billiard_problem:
    def __init__(self, initial_x=0.2, initial_y=0, initial_vx=0.8, initial_vy=0.3, time_step=0.01 ):
        self.dt=time_step
        self.x=[initial_x]
        self.y=[initial_y]
        self.vx=[initial_vx]
        self.vy=[initial_vy]
        self.t=[0]
    def run(self):
        for i in range(1,20000):
            self.x.append(self.x[i-1]+self.vx[i-1]*self.dt)
            self.y.append(self.y[i-1]+self.vy[i-1]*self.dt)
            self.vx.append(self.vx[i-1])
            self.vy.append(self.vy[i-1])
            if (self.x[i] > 1):
                self.vx[i]=-self.vx[i] 
            elif (self.x[i] < -1):
                self.vx[i]=-self.vx[i]
            elif (self.y[i] > 1):
                self.vy[i]=-self.vy[i] 
            elif (self.y[i] < -1):
                self.vy[i]=-self.vy[i]
            else:
                pass
            self.t.append(self.t[i-1]+self.dt)
        return self.x, self.y
    def show_results(self):
        pl.plot( self.x,self.y)
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.xlabel('$x$')
        pl.ylabel('$y$')
        pl.show()
a = billiard_problem()
a.run()
a.show_results()