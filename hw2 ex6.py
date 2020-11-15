#!/usr/bin/env python
# coding: utf-8

# In[86]:


import numpy as np
import matplotlib.pyplot as plt 

k=100
p=5000
a =np.random.normal(size=p)
A = np.diag(a)
A_inv=np.linalg.inv(A)
U=np.random.random((p, k))
V=np.random.random((k, p))
def woodbury(A, U, V):
    C =A_inv-A_inv@U@np.linalg.inv(np.linalg.inv(np.eye(k))+V@A_inv@U)@V@A_inv
    return C
import time

start1 = time.time()
m=woodbury(A, U, V)
end1 = time.time()
time1=(end1 - start1)
start2 = time.time()
h = np.linalg.inv(A+U@np.eye(k)@V)
end2 = time.time()
time2=(end2 - start2)

print(m-h)
print(time1-time2)
#быстрее будет вычисление по формуле Woodbury, насколько я поняла, прочитав про разные функции, много времени тратится на взятие обратной матрици, а в новом алгоритме мы берем ее от диагональной матрицы p*p, и от матрицы к*к, что быстрее, чем если берать ее от произвольной матрицы размера p*p


# In[77]:





# In[ ]:




