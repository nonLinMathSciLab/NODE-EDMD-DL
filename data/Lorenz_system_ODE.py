import random
import numpy as np
from numpy.random import *
from scipy.integrate import odeint


def Lorenz_system_ODE(x1range, x2range, x3range, numICs, tSpan, seed, type="z"):  # function X = PendulumFn(x1range, x2range, numICs, tSpan, seed, max_potential)
    # try some initial conditions for x1, x2
    np.random.seed(seed=seed)

    p, r, b = 10, 28, 8 / 3
    def dynsys(x, t):
        dydt = np.zeros_like(x)
        dydt[0] = -p * x[0] + p * x[1]
        dydt[1] = -x[0] * x[2] + r * x[0] - x[1]
        dydt[2] = x[0] * x[1] - b * x[2]
        return dydt

    lenT = len(tSpan)  # 11, 500

    X = np.zeros((numICs * lenT, 3))

    if type == "y":
        lenT = len(tSpan) - 1
        count = 1
        for j in range(100 * numICs):  # j = 1:100*numICs
            x1 = uniform(x1range[0], x1range[1])
            x2 = uniform(x2range[0], x2range[1])
            x3 = uniform(x3range[0], x3range[1])
            ic = [x1, x2, x3]
            temp = odeint(dynsys, ic, tSpan)
            # [T, temp] = odeint(dynsys, ic, tSpan)
            temp = temp[1:]

            X[(count - 1) * lenT: lenT + (count - 1) * lenT, :] = temp
            if count == numICs:
                break
            count = count + 1

        X = X[10**4::20]
        return X


    if type == "x":
        count = 1
        for j in range(100 * numICs):  # j = 1:100*numICs
            x1 = uniform(x1range[0], x1range[1])
            x2 = uniform(x2range[0], x2range[1])
            x3 = uniform(x3range[0], x3range[1])
            ic = [x1, x2, x3]
            temp = odeint(dynsys, ic, tSpan)
            # [T, temp] = odeint(dynsys, ic, tSpan)

            X[(count - 1) * lenT: lenT + (count - 1) * lenT, :] = temp
            if count == numICs:
                break
            count = count + 1

        X = X[10 ** 4::20]
        return X

    if type == "z":
        count = 1
        for j in range(100 * numICs):  # j = 1:100*numICs
            x1 = uniform(x1range[0], x1range[1])
            x2 = uniform(x2range[0], x2range[1])
            x3 = uniform(x3range[0], x3range[1])
            ic = [x1, x2, x3]
            temp = odeint(dynsys, ic, tSpan)
            # [T, temp] = odeint(dynsys, ic, tSpan)

            X[(count - 1) * lenT: lenT + (count - 1) * lenT, :] = temp
            if count == numICs:
                break
            count = count + 1

        X = X[10 ** 4::20]
        return X

    if type == "w":
        count = 1
        for j in range(100 * numICs):  # j = 1:100*numICs
            x1 = uniform(x1range[0], x1range[1])
            x2 = uniform(x2range[0], x2range[1])
            x3 = uniform(x3range[0], x3range[1])
            ic = [x1, x2, x3]
            temp = odeint(dynsys, ic, tSpan)
            # [T, temp] = odeint(dynsys, ic, tSpan)

            X[(count - 1) * lenT: lenT + (count - 1) * lenT, :] = temp
            if count == numICs:
                break
            count = count + 1

        X = X[10 ** 4:]
        return X
