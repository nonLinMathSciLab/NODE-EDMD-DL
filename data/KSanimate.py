# This file contains code that has been modified from the original by Jeff Whitaker.
# The original code is licensed under the MIT License.
# Copyright (c) 2015 Jeff Whitaker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
from KS import KS
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L   = 1#16           # domain is 0 to 2.*np.pi*L
N   = 50#128          # number of collocation points
dt  = 0.005#0.5          # time step
diffusion = 1.0
ks = KS(L=L,diffusion=diffusion,N=N,dt=dt) # instantiate model

# define initial condition
#u = np.cos(x/L)*(1.0+np.sin(x/L)) # smooth IC
u = 0.01*np.random.normal(size=N) # noisy IC
# remove zonal mean
u = u - u.mean()
# spectral space variable.
ks.xspec[0] = np.fft.rfft(u)

# time stepping loop.
nmin = 1000; nmax = 5000
uu = []; tt = []
vspec = np.zeros(ks.xspec.shape[1], np.float)
x = np.arange(N)
fig, ax = plt.subplots()
line, = ax.plot(x, ks.x.squeeze())
ax.set_xlim(0,N-1)
ax.set_ylim(-3,3)
#Init only required for blitting to give a clean slate.
def init():
    global line
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# spinup
for n in range(nmin):
    ks.advance()

def updatefig(n):
    global tt,uu,vspec
    ks.advance()
    vspec += np.abs(ks.xspec.squeeze())**2
    u = ks.x.squeeze()
    line.set_ydata(u)
    print(n,u.min(),u.max())
    uu.append(u); tt.append(n*dt)
    return line,

ani = animation.FuncAnimation(fig, updatefig, np.arange(1,nmax+1), init_func=init,
                              interval=25, blit=True, repeat=False)
plt.show()

plt.figure()
# make contour plot of solution, plot spectrum.
ncount = len(uu)
vspec = vspec/ncount
uu = np.array(uu); tt = np.array(tt)
print(tt.min(), tt.max())
nplt = 200
plt.contourf(x,tt[:nplt],uu[:nplt],31,extend='both')
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar()
#plt.title('chaotic solution of the K-S equation')
plt.savefig("K-S_exact.png")
plt.savefig("K-S_exact.eps")

"""plt.figure()
plt.loglog(ks.wavenums,vspec)
plt.title('variance spectrum')
plt.ylim(0.001,10000)
plt.xlim(0,100)
"""
plt.show()
