#!/usr/bin/env python
# coding: utf-8

# In[13]:


def solve_quad(b, c):
    d = b ** 2 - 4 * c
    if d == b**2:
        x1 = -b
        x2 = c/x1
        return x1, x2
    elif d == 0:
        return - b / 2, -b/2
    elif d > 0:
        return (((- b - d ** 0.5) / 2), (- b + d ** 0.5) / 2)
    elif d < 0:
        x1real = - b / 2
        x2real = - b / 2
        x1image = (-d) ** 0.5 / 2
        x2image = - (-d) ** 0.5 / 2
        x1 = complex(x1real, x1image)
        x2 = complex(x2real, x2image)
        return x1, x2
    

from numpy import allclose   
variants = [{'b': 4.0, 'c': 3.0},
            {'b': 2.0, 'c': 1.0},
            {'b': 0.5, 'c': 4.0},
            {'b': 1e10, 'c': 3.0},
            {'b': -1e10, 'c': 4.0},]
for var in variants:
    x1, x2 = solve_quad(**var)
    print(allclose(x1*x2, var['c']))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




