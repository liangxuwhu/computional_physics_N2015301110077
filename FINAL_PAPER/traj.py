import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from lorentz import lorentz
from euler_2Ddy import euler2d

# Const
m = 9.109e-31
epsz = 1e-9/36*np.pi
muz = (4e-7)*np.pi


# Initial conditions
q = 1.602e-19*np.array([1,-1,1,-1,1,-1,1,-1,-1])
x0 = np.array([-20,0,20,20,20,0,-20,-20,0])
y0 = np.array([-20,-20,-20,0,20,20,20,0,0])
vx0 = np.array([5,5,0,0,-5,-5,0,0,0])
vy0 = np.array([0,0,5,5,0,0,-5,-5,0])

# lorentz force limits
# if a particle is out of the box, we elimitate it's contribution
x1 = -30
x2 = 30
y1 = -30
y2 = 30

# Define a vector to indicate if particule is still in the box
in_out = np.ones(len(q))
dt = 0.01
x, y, vx, vy = x0, y0, vx0, vy0
xx, yy = [x0], [y0]
while sum(in_out) != 0:
    F, Etot, Btot, Ey = lorentz(q, x, y, vx, vy, m, epsz, muz)
    ax = (in_out*F[0])/m
    ay = (in_out*F[1])/m
    x, y, vx, vy = euler2d(x, y, vx, vy, ax, ay, dt)
    # We remove particles that get out of the box
    for p in range(len(q)):
        if x[p] <= x1 or x[p] >= x2 or y[p] <= y1 or y[p] >= y2:
            in_out[p] = 0
        else:
            xx.append(x)
            yy.append(y)

# Plot retults
fig, ax = plt.subplots(1)
box = patches.Rectangle((x1, y1), (x2-x1), (y2-y1),linewidth=1, edgecolor='r',facecolor='w')
ax.add_patch(box)
plt.plot(xx, yy)
axes = plt.gca()
axes.set_xlim([x1-10, x2+10])
axes.set_ylim([y1-10, y2+10])
axes.set_title('The trajectory of eight particles')
plt.show()
