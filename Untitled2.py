#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


data = pd.read_csv("netflixData.csv")
data


# In[21]:


btm_to_top = data['Production Country'].value_counts().sort_values(ascending=False)
btm_to_top


# In[38]:


plot=data["Production Country"].value_counts().head(20).to_numpy()
label=data["Production Country"].value_counts().head(20).keys()
plt.figure(figsize=(40,10))
sns.set(font_scale=1.5)
plt.bar(label,plot)
plt.show


# In[ ]:




