#!/usr/bin/env python
# coding: utf-8

# jsjsjsjs

# In[25]:


total = 0.0
for i in range (10):
    total +=0.1
print(f"Expect result: 1.0\nActual Result: {total}")
    


# In[21]:


def iternum(n):
    result=1
    for i in range(n):
        result +=0.1
    for i in range(n):
        result -=0.1
    return result
iternum(10000)


# In[22]:


format(iternum(1000000000), '0.30f')

