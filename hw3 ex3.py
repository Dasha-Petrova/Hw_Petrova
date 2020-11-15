#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 
a = np . zeros ((15 , 28))
a [2: -2 ,1]=1; a [2 ,2:6]=1
a [2:7 ,6]=1; a [7: -2 ,7]=1
a [7 ,2:7]=1; a [ -3 ,2:7]=1
a [2: -2 ,10]=1; a [2: -2 ,14]=1
a [2: -2 ,18]=1; a [ -3 ,10:19]=1
a [12 ,21:27]=1; a [ 2,21:27]=1
a [2:13,26]=1; a [ 7,21:27]=1
rank = np.linalg.matrix_rank(a)
plt .imshow(a)
print(rank)
print(np.linalg.svd(a, full_matrices = True, compute_uv = True))


# In[36]:


from PIL import Image
image = Image.open("Снимок.PNG")
image.show()
import numpy as np
import matplotlib.pyplot as plt 
a = np . zeros ((15 , 28))
a [2: -2 ,1]=1; a [2 ,2:6]=1
a [2:7 ,6]=1; a [7: -2 ,7]=1
a [7 ,2:7]=1; a [ -3 ,2:7]=1
a [2: -2 ,10]=1; a [2: -2 ,14]=1
a [2: -2 ,18]=1; a [ -3 ,10:19]=1
a [12 ,21:27]=1; a [ 2,21:27]=1
a [2:13,26]=1; a [ 7,21:27]=1
plt .imshow(a)
rankA =np.linalg.matrix_rank(a)
U, S, V = np.linalg.svd(a, full_matrices = True, compute_uv = True)
B = np.zeros((len(U),len(V)))
for i in range(rankA):
        B+= S[i]*np.matrix((U.T)[i]).T* np.matrix((V)[i])
        plt.imshow(B)
        fig = plt.figure()

