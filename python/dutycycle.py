import numpy as np
import time
import sys
from io import StringIO
import matplotlib.pyplot as plt

x=np.arange(10)
V = (x%2)*5

n=100
duty =0.1
y = np.zeros(10)
y[x%2 == 0]=x[x%2 == 0]/2
y[x%2 != 0] = x[x%2 == 0]/2 +duty
# y = y*8
plt.step(y,V)
plt.xlabel('time [$\mu$s]')
plt.ylabel('voltage [V]')
plt.title ('Duty Cycle 90%')
plt.savefig('duty90.png')

