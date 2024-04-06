import warnings

warnings.filterwarnings('ignore')

from Lorenz_system_ODE import Lorenz_system_ODE
#from Discrete_Linear_ODE import Discrete_Linear_ODE
#from Linear_ODE import Linear_ODE
import csv
import numpy as np

numICs = 1#0000

x1range = [-2, 2]
x2range = [-2, 2]
x3range = [-2, 2]
#tSpan = np.arange(0, 2.5 + 0.1, 0.25)# np.arange(0, 125, 0.25)  # 0:0.02:1
tSpan = np.arange(0, 160 + 0.0001, 0.001)



def make_csv(filename, X):
    with open(filename, 'w') as csv_file:
        fieldnames = ['precision_x', 'precision_y', 'precision_z']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for i in range(len(X)):
            writer.writerow({'precision_x': X[i, 0], 'precision_y': X[i, 1], 'precision_z': X[i, 2]})





###############Discrete_Linear#############################
filenamePrefix = 'Lorenz_system_detailed'

#tSpan = np.arange(0, 12.5, 0.25)  # 0, 12.5, 0.25
tSpan = np.arange(0, 2100 - 0.0001, 0.001)  # 160
seed = 10
#tSpan = np.arange(0, 2.5 - 0.1, 0.25)
X_train = Lorenz_system_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "x") # 0, 2.5, 0.25
filename_train = filenamePrefix + '_train_x.csv'
make_csv(filename_train, X_train)

#seed = 10
tSpan = np.arange(0, 2100 + 0.0001, 0.001)
#tSpan = np.arange(0, 2.5 + 0.1, 0.25) # 0, 2.5 + 0.1, 0.25
X_train = Lorenz_system_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "y")
filename_train = filenamePrefix + '_train_y.csv'
make_csv(filename_train, X_train)

#seed = 1#1
#tSpan = np.arange(0, 12.5, 0.25)
tSpan = np.arange(0, 2100 + 0.0001, 0.001)
X_train = Lorenz_system_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "z")
filename_train = filenamePrefix + "_E_recon_50" + '.csv'
make_csv(filename_train, X_train)

#seed = 3
#tSpan = np.arange(0, 0.25 + 0.1, 0.25)  # 0, 12.5, 0.25
tSpan = np.arange(0, 100 + 0.001, 0.001)
X_train = Lorenz_system_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "w")
filename_train = filenamePrefix + "_E_eigfunc" + '.csv'
make_csv(filename_train, X_train)