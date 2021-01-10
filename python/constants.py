import numpy as np
import matplotlib.pyplot as plt

mm=1e-3
gr = 1e-3

D=0.08/1000 #[inch]
h = 249*mm
G = np.asarray([130E9,160E9])
m=20.5*gr
# M = 0.0753

l_sides = 105*mm 
l_center = 8*mm
l_sides = np.asarray([l_sides,l_sides]) #  length [mm] 
l = 2*l_sides[0] + l_center #  length [mm] 
l /=2

# l=238*mm/2

kappa = (G*np.pi*D**4)/(h*32)
# I_CM = M*((2*l)**2)/12
I = 2*m*l**2
# + I_CM
# I = 0.0007853341
T = 2*np.pi*np.sqrt(I/kappa)


# brownian uncertainty

T0 = 300
k_b = 1.380649e-23
noise = np.sqrt(k_b*T0/kappa)

e= 1.6e-19



VT = 0.026
c = k_b*T0/e *np.log(10)
Is = 1e12
I= np.arange(500000)/1000
vd = c*np.log10(I/Is)
vd1 = c/np.log(10)*(I/Is-1)


plt.plot(I,vd)
plt.plot(I,vd1)
