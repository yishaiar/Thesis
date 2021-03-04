
import numpy as np 
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))

def fonts_define(xtitle,ytitle,lgd,font=25):
    plt.xlabel(xtitle, fontsize=font)
    plt.ylabel(ytitle, fontsize=font)
    plt.rc('xtick', labelsize=font) 
    plt.rc('ytick', labelsize=font)
    plt.legend(lgd,loc=1, prop={'size': font})



time = 40000 #s
t=np.linspace(0,time,3000);

kappa = 2.5839284154826904e-06
I = 0.000487121
omega_0 = np.sqrt(kappa/I)
print (np.pi*2/omega_0)

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
xi = 0.01
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



fonts_define('time [s]',r'$\theta$ \ $\theta_{max}$',['Undamped','Underdamped','Critically damped','Overdamped'],font=40)

# plt.savefig('damp.png')
# 