import warnings

warnings.filterwarnings('ignore')

from Kuramoto_Sivashinsky_ODE import Kuramoto_Sivashinsky_ODE
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
        fieldnames = []
        for i in range(64):
            fieldnames.append('prediction_x' + "{stp:02}".format(stp=i))
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        dic = {}
        for i in range(len(X)):
            for j in range(64): #65
                dic[fieldnames[j]] = X[i][j]
            writer.writerow(dic)





###############Discrete_Linear#############################
filenamePrefix = 'Kuramoto_Sivashinsky2'

#tSpan = np.arange(0, 12.5, 0.25)  # 0, 12.5, 0.25
tSpan = np.arange(0, 2100 - 0.0001, 0.001)  # 160
seed = 10
#tSpan = np.arange(0, 2.5 - 0.1, 0.25)
X_train = Kuramoto_Sivashinsky_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "x") # 0, 2.5, 0.25
filename_train = filenamePrefix + '_train_x.csv'
make_csv(filename_train, X_train)

#seed = 10
tSpan = np.arange(0, 2100 + 0.0001, 0.001)
#tSpan = np.arange(0, 2.5 + 0.1, 0.25) # 0, 2.5 + 0.1, 0.25
X_train = Kuramoto_Sivashinsky_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "y")
filename_train = filenamePrefix + '_train_y.csv'
make_csv(filename_train, X_train)

#seed = 1#1
#tSpan = np.arange(0, 12.5, 0.25)
tSpan = np.arange(0, 2100 + 0.0001, 0.001)
X_train = Kuramoto_Sivashinsky_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "z")
filename_train = filenamePrefix + "_E_recon_50" + '.csv'
make_csv(filename_train, X_train)

#seed = 3
#tSpan = np.arange(0, 0.25 + 0.1, 0.25)  # 0, 12.5, 0.25
tSpan = np.arange(0, 100 + 0.001, 0.001)
X_train = Kuramoto_Sivashinsky_ODE(x1range, x2range, x3range, numICs, tSpan, seed, "w")
filename_train = filenamePrefix + "_E_eigfunc" + '.csv'
make_csv(filename_train, X_train)