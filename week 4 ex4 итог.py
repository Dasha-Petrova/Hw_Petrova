#!/usr/bin/env python
# coding: utf-8

# In[261]:


#обратная итерация с m = 3.5
import numpy as np
q = np.random.uniform(0, 1, 4)
a = np.array([[3, 1, 0, 0],
              [1, 2, 0, 1],
              [0, 0, 1, 1],
              [0, 1, 1, 1]])
e = 1
k=0
m =3.5
#единичная матрица:
eye = np.eye(4)
while np.linalg.norm(e) > 0.001:
    r =np.dot(np.linalg.inv(a-m*eye),q)
    r=r/np.linalg.norm(r)
    e = np.linalg.norm(q-r)
    q=r
    k+=1
mb= np.dot(r,(a@r))/np.dot(r,r)

print("Наибольшее собственное число =",mb)
print("Соответствующее ему значение собственного вектора, полученное в ходе итераций =", q)
print("Количество итераций", k)


# In[262]:


#обратная итерация с m = 3.6
import numpy as np
q = np.random.uniform(0, 1, 4)
a = np.array([[3, 1, 0, 0],
              [1, 2, 0, 1],
              [0, 0, 1, 1],
              [0, 1, 1, 1]])
e = 1
k=0
m =3.6
#единичная матрица:
eye = np.eye(4)
while np.linalg.norm(e) > 0.001:
    r =np.dot(np.linalg.inv(a-m*eye),q)
    r=r/np.linalg.norm(r)
    e = np.linalg.norm(q-r)
    q=r
    k+=1
mb= np.dot(r,(a@r))/np.dot(r,r)
print("Наибольшее собственное число =",mb)
print("Соответствующее ему значение собственного вектора, полученное в ходе итераций =", q)
print("Количество итераций", k)


# In[1]:


#Степенная итерация 
import numpy as np
q = np.random.uniform(0, 1, 4)
a = np.array([[3, 1, 0, 0],
              [1, 2, 0, 1],
              [0, 0, 1, 1],
              [0, 1, 1, 1]])
e = 1
k=0
while np.linalg.norm(e) > 0.001:
    r = a@q/np.linalg.norm(a@q)
    e=np.linalg.norm(q-r)
    m= np.dot(r,(a@r))/np.dot(r,r)
    q=r
    k+=1
print("Наибольшее собственное число =",m)
print("Соответствующее ему значение собственного вектора, полученное в ходе итераций =", q)
print("Количество итераций", k)


# In[306]:


import numpy as np
ma=[]
ka=[]
m =3.3

def iterfunk(m):
    q = np.random.uniform(0, 1, 4)
    a = np.array([[3, 1, 0, 0],
                  [1, 2, 0, 1],
                  [0, 0, 1, 1],
                  [0, 1, 1, 1]])
    e = 1
    k=0
    eye = np.eye(4)
    while np.linalg.norm(e) > 0.001:
        r =np.dot(np.linalg.inv(a-m*eye),q)
        r=r/np.linalg.norm(r)
        e = np.linalg.norm(q-r)
        q=r
        k+=1
    return(k)
while m<=3.7:
    ka.append(iterfunk(m))
    ma.append(m)
    m+=0.05
import matplotlib.pyplot as plt
plt.plot(ma, ka)
plt.grid()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




