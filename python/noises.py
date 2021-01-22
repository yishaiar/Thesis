# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

A = 1.14E-2
P = 1E-4*100
T = 298.0
T_0 = 288.0
N_A = 6.022E23
R = 8.314
# mu_298k = 1.85e-5*np.sqrt()
# bolzman
SIGMA = 5.67E-8
EPSILON =0.03
p =SIGMA  *EPSILON*A*(T**4-T_0**4)
print(p)

# thermal
C_V = 0.716E3
M =28.9647e-3
m = M/N_A

p = np.sqrt(M/(R*T))*C_V*A*P*(T-T_0)
print(p)


# BROWNIAN

p = 6/N_A*np.sqrt(P*A*R*T*np.sqrt(3*R*T/M))
print(p)

v = np.sqrt(3*R*T/M)

# ACOUSTIC
c=1e-22
p = A*P**2*c
print(p)


k=1.38e-23

T1=299
T0=np.arange(T1*100)/100.0
T = np.ones(T1*100)*298.0

p=SIGMA*EPSILON*A*(T**4-T0**4)+np.sqrt(M/(R*T1))*C_V*A*P*(T-T0)

plt.plot(T0,p)



max_tourqe = 6.8e-10
THETA_MAX=1E-6
OMEGA = 2*np.pi/84
p = max_tourqe/2*THETA_MAX*OMEGA 
# # ACOUSTIC
# rho = M*P/(R*T)
# k_s = 142E3
# p = A*P*np.sqrt(k_s/rho)