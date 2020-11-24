#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
from scipy.linalg import expm
def cron(i,j):
    if i == j:
        return 1
    if i != j:
        return 0
A=np.zeros((32,32))
for i in range(32):
        for j in range(32):
            A[i,j]=-cron(i,j)+cron(i,j-1)+cron(i,j-2)
T=[]
EXP=[]
t=0
while t < 50:
    T.append(t)
    EXP.append(np.linalg.norm(expm(A*t), ord='fro'))
    t+=1
import matplotlib.pyplot as plt
plt.scatter(T, EXP)
plt.grid()
plt.show()


# In[32]:


i=1
while i <= 5:
    X = []
    Y = []
    for x in np.arange(-5,5, 0.01):
        for y in np.arange(-5,5, 0.01):
            z = complex(x,y)
            D = z*np.eye(32)- A
            U,S,VT = np.linalg.svd(D)
            if np.min(S) <= 10**(-i):
                X.append(x)
                Y.append(y)
    plt.scatter(X,Y)
    i += 1


# In[ ]:




