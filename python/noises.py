# -*- coding: utf-8 -*-
import numpy as np
A = 1.14E-2
P = 1E-4*100
T = 298
N_A = 6.022E23
R = 8.314
# bolzman
SIGMA = 5.67E-8
EPSILON =0.075
p =SIGMA  *EPSILON*A*T**4
# thermal
C_V = 0.716E3
M =28.9647e-3
m = M/N_A

p = np.sqrt(M/(R*T))*C_V*A*P*T


# BROWNIAN

p = 6/N_A*np.sqrt(P*A*R*T*np.sqrt(3*R*T/M))

v = np.sqrt(3*R*T/M)

# ACOUSTIC
rho = M*P/(R*T)
k_s = 142E3
p = A*P*np.sqrt(k_s/rho)