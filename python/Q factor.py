import numpy as np
import matplotlib.pyplot as plt

def plot_q(n =int(1e5+1), p=1e-20):
    initaial = -3
    final = -20
    theta = 10**(np.arange(n)[::-1]/(n-1)*(initaial - final)+final )
    kappa = 2.7e-6
    T=86
    tau=6.8e-10
    if isinstance(p, float):
        p= np.ones([n])*p
    Q = np.pi/T*( (kappa*(theta**2)) / (theta*np.pi*tau/T-p))
    for i,q in enumerate(Q):
        if q<0:
            break
    theta = theta[:i]
    Q = Q[:i]
    plt.plot(theta,Q)
    
    ones = np.ones([i])
    plt.plot(theta,ones*0.5)
    plt.plot(theta,ones*1)
    plt.plot(theta,ones*0)
    
    plt.yscale('log')
    plt.xscale('log')

plot_q(n =int(1e5+1), p=3.6e-14)
        






# plt.gca().invert_xaxis()

