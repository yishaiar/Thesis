import numpy as np

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




