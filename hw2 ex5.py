#!/usr/bin/env python
# coding: utf-8

# In[2]:



import numpy as np

def diy_lu(a):
    """Создает LU - разложение матрицы `a`.
    
    Наивное LU - разложение: работает столбец за столбцом, накапливает элементарные треугольные матрицы.
    Без выбора главного элемента.
    """
    N = a.shape[0]
    
    u = a.copy()
    L = np.eye(N)
    for j in range(N-1):
        lam = np.eye(N)
        gamma = u[j+1:, j] / u[j, j]
        lam[j+1:, j] = -gamma
        u = lam @ u

        lam[j+1:, j] = gamma
        L = L @ lam
    return L, u


# In[4]:



# Теперь сгенерируем матрицу полного ранга и протестируем наивное разложение.
import numpy as np

N = 6
a = np.zeros((N, N), dtype=float)
for i in range(N):
    for j in range(N):
        a[i, j] = 3. / (0.6*i*j + 1)

np.linalg.matrix_rank(a)


# In[5]:


# Настройка вывода чисел с плавающей точкой для большей ясности
np.set_printoptions(precision=3)


# In[7]:


L, u = diy_lu(a)

print(L, "\n")
print(u, "\n")

# Быстрый тест на адекватность: L @ U должна быть равна изначальной матрице с точностью до ошибок округления.
print(L@u - a)

