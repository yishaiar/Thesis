import numpy as np
import time
import sys
from io import StringIO
import matplotlib.pyplot as plt
N=20
x=np.arange(N)
# y = np.zeros(N)

V = (x%2)*5

duty =0.8
y=[]
for i in x:
    if i%2 == 0:
        y.append(i/2)
    else:
        y.append(y[-1]+duty)
    if i%int(N/2) == 0 and i !=0:
        duty =0.2
# y[x%2 == 0]=x[x%2 == 0]/2
# y[x%2 != 0] = x[x%2 == 0]/2 +duty
# y = y*8
plt.step(y,V)
plt.xlabel('time [$\mu$s]')
plt.ylabel('voltage [V]')
# plt.title ('Duty Cycle 90%')
plt.savefig('duty90.png')

