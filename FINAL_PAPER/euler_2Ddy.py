def euler2d(x, y, vx, vy, ax, ay, dt):
    x_next = x+dt*vx
    y_next = y+dt*vy
    vx_next = vx+dt*ax
    vy_next = vy+dt*ay
    return x_next, y_next, vx_next, vy_next