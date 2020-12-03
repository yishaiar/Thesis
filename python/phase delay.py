import numpy as np

import matplotlib.pyplot as plt


t0 = 3
t_samp = 0.008
omega = 2*np.pi/86
t = (np.arange(2*10750)-10750)*t_samp
x= np.cos(t*omega)
y = np.cos((t-t0)*omega)


z=[]
for Y,X in zip(y,x):
    if Y>0.75 or Y<-0.75:
        z.append(0)
    else:
        tmp =  (Y-X)/X
        if tmp>2:
            tmp = 0
        if tmp<-2:
            tmp = 0
        z.append(tmp)
        

# plt.plot(t,x)
# plt.plot(t,y)
plt.plot(t,z,'.')

