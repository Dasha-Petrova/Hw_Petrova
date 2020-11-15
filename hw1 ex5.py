#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
def round_to_n(x,n):
    if x == 0:
        return x
    else:
        return round (x, -int(math.floor(math.log10(abs(x))))+(n - 1))
print(round_to_n(1.12342355432345, 10))


# In[14]:


#тут мы 3000 раз теряем что-то порядка 10^-4, что нам потом как раз и портит конечный ответ
res = 0
for k in range (1 ,3001):
    res = round_to_n ( res +1/ k **2 , 4)
print(res)


# In[13]:


#тут мы 1 раз теряем что-то порядка 10^-4, что нам потом как раз и позволяет получить большую точность
res = 0
for k in range (1 ,3001):
    res = res +1/ k **2 
print(round_to_n (res,5))

