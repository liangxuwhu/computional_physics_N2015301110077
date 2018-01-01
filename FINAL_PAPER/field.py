import numpy as np
def field(q, x0, y0, vx0, vy0, m, epsz, muz):
    E = np.zeros((len(q), len(q)))
    B = np.zeros((len(q), len(q)))
    theta = np.zeros((len(q), len(q)))
    for ii in range(len(q)):
        for jj in range(len(q)):
            if ii == jj:
                E[ii][jj] = 0
                B[ii][jj] = 0
                theta[ii][jj] = 0
            else:
                vect_i2j = np.array([x0[jj]-x0[ii], y0[jj]-y0[ii],0])
                qv = q[jj]*np.array([vx0[jj], vy0[jj],0])
                rhat = vect_i2j / np.linalg.norm(vect_i2j)
                E[ii][jj] = q[jj] / (4*np.pi*epsz*(vect_i2j[0]**2+vect_i2j[1]**2))
                theta[ii][jj] = np.arctan2(vect_i2j[1], vect_i2j[0])
                B[ii][jj] = (muz*sum(np.cross(qv, rhat))) / (4*np.pi*(vect_i2j[0]**2+vect_i2j[1]**2))
    return E, B, theta
