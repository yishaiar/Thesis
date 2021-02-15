import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))

def fonts_define(xtitle,ytitle,lgd,font=25):
    plt.xlabel(xtitle, fontsize=font+2)
    plt.ylabel(ytitle, fontsize=font+2)
    plt.rc('xtick', labelsize=font) 
    plt.rc('ytick', labelsize=font)
    plt.legend(lgd,loc=2, prop={'size': 20})
def Q(p=1E-18, ones = False):
    n =int(1e5+1)
    initaial = -4
    final = -9
    theta = 2.5*10**(np.arange(n)[::-1]/(n-1)*(initaial - final)+final )
    kappa = 2.7e-6
    T=40
    tau=3.4e-10
    p=np.ones([n])*p
    
    Q = np.pi/T*( (kappa*(theta**2)) / (theta*np.pi*tau/T-p))
    # for i,q in enumerate(Q):
    #     if q<0:
    #         break
    # theta = theta[:i]
    # Q = Q[:i]
    # ones = np.ones([i])
    plt.plot(theta,Q)

    if ones:
        ones = np.ones(theta.shape[0])
        
        plt.plot(theta,ones*0.5)
        plt.plot(theta,ones*1)
    # plt.plot(theta,ones*1e-9)
    
    plt.yscale('log')
    plt.xscale('log')
Q(p=1.3E-18 )
Q(p=8E-18,ones=True )
fonts_define(r'$\theta_{max} [rad]$','Q factor',[r'$Q(p=1E-18)$',r'$Q(p=8E-18)$','Q = 0.5','Q = 1'],font=25)

plt.savefig('Q factor.png')
        






# plt.gca().invert_xaxis()

