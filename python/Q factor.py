import numpy as np
import matplotlib.pyplot as plt

n =int(1e5+1)
initaial = -4
final = -9
theta = 2.5*10**(np.arange(n)[::-1]/(n-1)*(initaial - final)+final )
kappa = 2.7e-6
T=40
tau=6.8e-10
p=np.ones([n])*1E-18

Q = np.pi/T*( (kappa*(theta**2)) / (theta*np.pi*tau/T-p))
# for i,q in enumerate(Q):
#     if q<0:
#         break
# theta = theta[:i]
# Q = Q[:i]
# ones = np.ones([i])

ones = np.ones(theta.shape[0])
plt.plot(theta,Q)

plt.plot(theta,ones*0.5)
# plt.plot(theta,ones*1)
# plt.plot(theta,ones*1e-9)

plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$\theta_{max}$')
plt.ylabel(r'$\theta$')
plt.legend(['Q factor','Critically damped'])


        






# plt.gca().invert_xaxis()

