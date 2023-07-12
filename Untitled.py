#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data=list()
import pandas as pd
import os
path = "C:/Users/l.hamwi/OneDrive - Saudi Electronic University/archive sample"
for (root,dirs,file) in os.walk(path):
    for x in file:
        #print(x)
        data.append(x)
        
df1=pd.DataFrame(data)


# In[ ]:


print(df1)


# In[ ]:


df1[0]= df1[0].str.replace('ArchiveFile_','')
df1[0]= df1[0].str.replace('.zip','')


# In[ ]:


df1['EXTERNAL_COURSE_KEY']=''
df1['AVAILABLE_IND']='N'
df1['ROW_STATUS']='enabled'


# In[ ]:


df1.columns=['COURSE_ID','EXTERNAL_COURSE_KEY','AVAILABLE_IND','ROW_STATUS']
df1['EXTERNAL_COURSE_KEY']=df1['COURSE_ID'].str[-6:]+'.'+df1['COURSE_ID'].str[-12:-7]


# In[ ]:


df1


# In[ ]:


df1.to_csv('mylist.csv', index=False)


# In[ ]:




