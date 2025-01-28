#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.hstack((arr1,arr2))
print(result)


# In[3]:


import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.vstack((arr1,arr2))
print(result)


# In[4]:


import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.dstack((arr1,arr2))
print(result)


# In[7]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
result=np.split(arr,3)
print(result)


# In[ ]:




