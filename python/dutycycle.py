import numpy as np
import time
import sys
from io import StringIO
import matplotlib.pyplot as plt

f=16e6
b=2**8
T = b/f/1E-6

T1 = 1/500/1E-6
N=60
x=np.arange(N)
# y = np.zeros(N)

V = (x%2)*5

duty =0.1 + np.arange(4)*(0.9-0.1)/3
y=[]

counter = 0
for i in x:
    if i%2 == 0:
        y.append((i/2)*T)
    else:
        y.append(y[-1]+duty[counter]*T)
    if counter*T+ i%T <i :
        counter += 1
        print(duty[counter])
y = np.asarray(y)
pw = y[1:]-y[:-1]
pw[1::2]=0
pw[1::2] = pw[:-1:2] 
pw *=(5/T)
pw = np.concatenate(([pw[0]], pw))
# y = np.asarray(y)*T
# y[x%2 == 0]=x[x%2 == 0]/2
# y[x%2 != 0] = x[x%2 == 0]/2 +duty
# y = y*T
plt.figure(figsize=(20,10))
plt.step(y,V)
plt.step(y,pw)
plt.xlabel('time [$\mu$s]')
plt.ylabel('voltage [V]')
plt.legend()
plt.legend(['Digital voltage','Analog voltage'],loc=2, prop={'size': 20})

# plt.title ('Duty Cycle 90%')
plt.savefig('duty_cycle.png')

