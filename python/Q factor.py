import numpy as np
import matplotlib.pyplot as plt

n = int(1e5)
initaial = -5
final = -20
theta = 10**(np.arange(n)/n*(initaial - final)+final )

p=1e-30
kappa = 2.7e-6
T=86
tau=6.8e-10
Q = np.pi/T*( (kappa*(theta**2)) / (theta*np.pi*tau/T-p))
for i,q in enumerate(Q):
    if q>0:
        break
theta = theta[i:]
Q = Q[i:]
        

ones = np.ones([n])

plt.plot(theta,Q)
# plt.plot(theta,ones*0.5)
# plt.plot(theta,ones*1)
# plt.plot(theta,ones*0)


# plt.yscale('symlog')
# plt.xscale('log')
# plt.gca().invert_xaxis()

