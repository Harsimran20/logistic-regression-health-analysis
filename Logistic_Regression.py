#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score


# In[14]:


heart_df = pd.read_csv("C:/Users/ACER/Downloads/archive (10)/heart.csv")


# In[26]:


heart_df.columns
heart_df.info()
heart_df['target'].nunique()
heart_df.head()


# In[34]:


X = heart_df.drop('target',axis = 1)
y = heart_df["target"]


# In[38]:


X.head()


# In[40]:


y.head()


# In[46]:


X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size = 0.2 , random_state = 42
)


# In[58]:


y_train[y_train == 1]
y_train[y_train == 0]


# In[56]:


model = LogisticRegression(max_iter = 1000)
model.fit(X_train,y_train)


# In[60]:


y_pred = model.predict(X_test)


# In[66]:


print("Accuracy Score:",accuracy_score(y_test,y_pred)*100,"%")


# In[68]:


print("Precision Score:",precision_score(y_test,y_pred)*100,"%")


# In[ ]:




