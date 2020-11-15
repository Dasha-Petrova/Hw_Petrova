#!/usr/bin/env python
# coding: utf-8

# In[45]:


# обратная рекурсия для 0.1
a1 = 10
I0_10 = 0
for n in reversed(a):
    I0_10 = 1 / a1 / n - I0_10 / a1
    print(I0_10)


# In[47]:


# обратная рекурсия для 0.1
a1 = 0.1
I0_10 = 0
for n in reversed(a):
    I0_10 = 1 / a1 / n - I0_10 / a1
    print(I0_10)


# In[50]:


# прямая рекурсия для 10
import math
a1 = 10
I0_10 = math.log(11/10)
for n in range(1, 25):
    I0_10 = 1 / n - a1*I0_10
    print(I0_10)


# In[51]:


# прямая рекурсия для 0.1
import math
a2 = 0.1
I0_10 = math.log(11/10)
for n in range(1, 25):
    I0_10 = 1 / n - a2*I0_10
    print(I0_10)

