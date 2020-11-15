#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a = np.array([[3, 0],
              [0, -2]])
a_t=np.transpose(a)
V_0= np.matmul(a_t, a)
U_0= np.matmul(a, a_t)
l0, U= np.linalg.eig(U_0)
l0, V = np.linalg.eig(V_0)
l = l0**0.5
print(U, l, V)
np.linalg.svd(a, full_matrices = True, compute_uv = True)


# In[4]:


import numpy as np
a = np.array([[0, 2],
              [0, 0],
              [0, 0]])
a_t=np.transpose(a)
V_0= np.matmul(a_t, a)
U_0= np.matmul(a, a_t)
l0, U= np.linalg.eig(U_0)
l0, V = np.linalg.eig(V_0)
l = l0**0.5
print(V)
np.linalg.svd(a, full_matrices = True, compute_uv = True)


# In[3]:


import numpy as np
a = np.array([[1, 1],
              [1, 1]])
a_t=np.transpose(a)
V_0= np.matmul(a_t, a)
U_0= np.matmul(a, a_t)
l0, U= np.linalg.eig(U_0)
l0, V = np.linalg.eig(V_0)
l = l0**0.5
np.linalg.svd(a, full_matrices = True, compute_uv = True)

