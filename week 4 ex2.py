#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 
from numpy import linalg as LA
n=10
a = np.random.normal(0, 1, (n, n))
A = a @a.T
l = LA.eigvalsh(A)
for i in range(100): 
    Q, R= LA.qr(A)
    Anew =R.dot(Q)
    A = Anew
    i+=1
    #A[9][9] будет соответствовать наименьшему собственному числу
    if (abs(l[0]-A[9][9]))/l[0] <= 0.01:
        break
print(i)


# In[ ]:





# In[ ]:





# In[ ]:




