import random
import numpy as np
from numpy.random import *
#from scipy.integrate import odeint


def Kuramoto_Sivashinsky_ODE(x1range, x2range, x3range, numICs, tSpan, seed, type="z"):  # function X = PendulumFn(x1range, x2range, numICs, tSpan, seed, max_potential)
    # try some initial conditions for x1, x2
    import numpy as np
    np.random.seed(seed=seed)

    # -*- coding: utf-8 -*-
    """
    Created on Tue Oct 15 15:09:30 2019

    @author: Masaua Muramatsu
    """

    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    Lx = 35#35
    Nx = 63#64#64
    dx = Lx / Nx
    dt = 0.0025#0.0025
    tmax = 100
    # Nt = 10
    Nt = int(tmax / dt)
    now_u = np.zeros(Nx + 4)
    du = np.zeros(Nx + 4)
    new_u = np.zeros(Nx + 4)
    u = np.zeros((Nt, Nx + 4))
    v = np.zeros((Nt, Nx + 1))
    if type == "z":
        np.random.seed(2)
    elif type == "w":
        np.random.seed(3)
    else:
        np.random.seed(1)
    # 初期条件
    for i in range(Nx + 2):
        now_u[i] = np.random.rand()

    u[0, :] = now_u

    for i in range(1, Nt):

        for j in range(2, Nx + 2):
            du[j] = -(now_u[j + 1] - 2 * now_u[j] + now_u[j - 1]) / (dx ** 2) - (
                        now_u[j + 2] - 4 * now_u[j + 1] + 6 * now_u[j] - 4 * now_u[j - 1] + now_u[j - 2]) / (dx ** 4) - \
                    now_u[j] * (now_u[j + 1] - now_u[j - 1]) * 0.5 / dx

        now_u[0] = now_u[Nx]
        now_u[1] = now_u[Nx + 1]
        now_u[Nx + 2] = now_u[2]
        now_u[Nx + 3] = now_u[3]

        new_u = now_u + du * dt
        u[i, :] = np.array(new_u)

        now_u = new_u

    for i in range(1, Nx + 2):
        v[:, i - 1] = (u[:, i] + u[:, i + 1]) / 2

    x = list(range(Nt))
    y = list(range(Nx + 1))

    X, Y = np.meshgrid(x, y)

    def functz(u):
        z = u[X, Y]
        return z

    Z = functz(v)

    """
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('U')
    plt.show()
    """
    t = np.arange(0, tmax, dt)
    for i in range(Nt):
        X[:, i] = t[i]

    plt.pcolormesh(Y, X, Z, cmap='hsv')  # 等高線図の生成。cmapで色付けの規則を指定する。
    pp = plt.colorbar(orientation="vertical")  # カラーバーの表示 
    pp.set_label("Label", fontname="Arial", fontsize=10)  # カラーバーのラベル

    plt.xlabel('x', fontsize=10)
    plt.ylabel('t', fontsize=10)

    plt.show()

    return Z.T
