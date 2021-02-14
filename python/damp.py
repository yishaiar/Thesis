
import numpy as np 
import matplotlib.pyplot as plt

t=np.linspace(0,200,3000);

kappa = 2.5839284154826904e-06
I = 0.000487121
omega_0 = np.sqrt(kappa/I)

theta_max = 1
vo=0; 
x0=theta_max

# undamped
xi = 0.0
# tao = 1/(xi*omega_0)

a=x0;
xt=a*np.cos(omega_0*t);
plt.plot(t,xt)


# underdamped
xi = 0.1
tao = 1/(xi*omega_0)

a=x0;
omega = omega_0*np.sqrt(1-xi**2)
xt=a*(np.exp(-t/tao))*np.cos(omega*t);
plt.plot(t,xt)

# critical
xi = 1.0
tao = 1/(xi*omega_0)
 
a=x0;
b=x0/tao;
xt=(a+b*t)*(np.exp(-t/tao));
plt.plot(t,xt)




# overdamped
xi = 1.5
tao = 1/(xi*omega_0)
xi_1 = xi/np.sqrt(xi**2-1)
a = (1-xi_1)
a_exp = 1+1/xi_1
b = (1+xi_1)
b_exp = 1-1/xi_1

xt=x0/2*(a*np.exp(-t/tao*a_exp)+b*np.exp(-t/tao*b_exp))
plt.plot(t,xt)


plt.ylabel(r'$\theta$ \ $\theta_{max}$')
plt.xlabel ('t [s]')
plt.legend(['Undamped','Underdamped','Critically damped','Overdamped'])

# plt.savefig('damp.png')
# 