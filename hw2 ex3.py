#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
a = np.array([[-3, 0],
              [0, 2]])
U, L, Vt = np.linalg.svd(a, full_matrices = True, compute_uv = True)
u1, u2 = U
v1, v2 = np.transpose(Vt)
l1, l2 = L
print(l1, l2)
import matplotlib.pyplot as plt 
plt.arrow(0, 0, *u1, color = 'red')
plt.arrow(0, 0, *u2, color = 'blue')
phi = np.arange (0, 1*np.pi, 0.01)
plt.scatter( np.cos(phi),np.sin(phi), 0.2, color = 'green')
plt.scatter( -np.cos(phi),-np.sin(phi), 0.2, color = 'green')
plt.xlim(-max(l1, l2) ,max(l1, l2))
plt.ylim(-max(l1, l2),max(l1, l2))
plt.grid()


# In[78]:


import matplotlib.pyplot as plt 
plt.arrow(0, 0, *v1, color = 'red')
plt.arrow(0, 0, *v2, color = 'blue')
phi = np.arange (0, 1*np.pi, 0.01)
plt.scatter( np.cos(phi),np.sin(phi), 0.2, color = 'green')
plt.scatter( -np.cos(phi),-np.sin(phi), 0.2, color = 'green')
plt.xlim(-max(l1, l2) ,max(l1, l2))
plt.ylim(-max(l1, l2),max(l1, l2))
plt.grid()


# In[ ]:




