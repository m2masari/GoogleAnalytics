#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import datetime
import datetime


# In[3]:


start_date = datetime.date(2023, 1, 2)
today= datetime.date.today()


# In[5]:


start_date = datetime.date(2023, 1, 2)
today= datetime.date.today()
date_list = []


# In[6]:


def date_range(start_date):
    return [{"startDate": start_date.strftime("%Y-%m-%d"),
             "endDate": (start_date + datetime.timedelta(days=6.9)).strftime("%Y-%m-%d")}]


# In[7]:


date_range(start_date)


# In[8]:


while start_date<today:
      date_list.append(date_range(start_date))
      start_date= (start_date + datetime.timedelta(days=7.9))


# In[9]:


for date_item in date_list:
    date_range = date_item[0]
    startDate = date_range['startDate']
    endDate = date_range['endDate']
    print(startDate,endDate)


# In[ ]:




