import random
import numpy as np
from numpy.random import *
#from scipy.integrate import odeint

import os
import argparse
import time
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
import cloudpickle

import numpy as np
from scipy import linalg as la

from matplotlib.colors import Normalize # Normalizeをimport
from matplotlib import pyplot as plt
from scipy.stats import uniform

def K_S_FFT_ODE(x1range, x2range, x3range, numICs, tSpan, seed, type="z"):  # function X = PendulumFn(x1range, x2range, numICs, tSpan, seed, max_potential)
    import numpy as np
    from KS import KS
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    L = 16  # domain is 0 to 2.*np.pi*L
    N = 128  # number of collocation points
    dt = 0.5  # time step
    diffusion = 1.0
    ks = KS(L=L, diffusion=diffusion, N=N, dt=dt)  # instantiate model

    # define initial condition
    # u = np.cos(x/L)*(1.0+np.sin(x/L)) # smooth IC
    def data_Preprocessing(tr_val_te, cut):
        data = np.loadtxt(('%s_%s.csv' % ("K_S_FFT", tr_val_te)), delimiter=',', dtype=np.float64)[:cut]
        # np.loadtxt(('./data/%s_val_x.csv' % (params['data_name'])), delimiter=',', dtype=np.float64)  # ここでデータを読み込む
        data = torch.tensor(data, dtype=torch.float32).detach().numpy()
        return data

    if type == "z":
        data = data_Preprocessing("E_recon_50", 100000) #data[n][i]
        for n in range(len(data)):
            for i in range(128):
                if n < 38:
                    data[n][i] = data[n][i] + 0.5 * np.random.normal(size=1)[0]
                else:
                    data[n][i] = data[n][i] + 1 * np.random.normal(size=1)[0]
        return data
    """if type == "w":
        np.random.seed(seed=33)"""
    u = 0.01 * np.random.normal(size=N)  # noisy IC
    # remove zonal mean
    u = u - u.mean()
    # spectral space variable.
    ks.xspec[0] = np.fft.rfft(u)

    # time stepping loop.
    nmin = 1000;
    nmax = 5000
    uu = [];
    tt = []
    vspec = np.zeros(ks.xspec.shape[1], np.float)
    x = np.arange(N)
    fig, ax = plt.subplots()
    line, = ax.plot(x, ks.x.squeeze())
    ax.set_xlim(0, N - 1)
    ax.set_ylim(-3, 3)

    # Init only required for blitting to give a clean slate.
    def init():
        global line
        line.set_ydata(np.ma.array(x, mask=True))
        return line,

    # spinup
    for n in range(nmin):
        ks.advance()

    def updatefig(n):
        global tt, uu, vspec
        ks.advance()
        vspec += np.abs(ks.xspec.squeeze()) ** 2
        u = ks.x.squeeze()
        line.set_ydata(u)
        print(n, u.min(), u.max())
        uu.append(u);
        tt.append(n * dt)
        return line,

    ani = animation.FuncAnimation(fig, updatefig, np.arange(1, nmax + 1), init_func=init,
                                  interval=25, blit=True, repeat=False)
    plt.show()

    plt.figure()

    # make contour plot of solution, plot spectrum.
    ncount = len(uu)
    vspec = vspec / ncount
    uu = np.array(uu);
    tt = np.array(tt)
    print(tt.min(), tt.max())
    nplt = 200
    plt.contourf(x, tt[:nplt], uu[:nplt], 31, extend='both')
    plt.xlabel('x')
    plt.ylabel('t')
    plt.colorbar()
    plt.title('chaotic solution of the K-S equation')
    plt.savefig("K-S_exact.png")
    plt.savefig("K-S_exact.eps")

    """plt.figure()
    plt.loglog(ks.wavenums,vspec)
    plt.title('variance spectrum')
    plt.ylim(0.001,10000)
    plt.xlim(0,100)
    """
    z = uu[:nplt]
    z = np.array(z)
    return z.T

