#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BeautifulSoup + Requests


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = 'https://www.scrapethissite.com/pages/forms/'


# In[4]:


page = requests.get(url)


# In[5]:


soup = BeautifulSoup(page.text, 'html')


# In[6]:


print(soup)


# In[7]:


# Find and Find_All


# In[8]:


soup.find('div')


# In[9]:



soup.find_all('p', class_ = 'lead')


# In[10]:


soup.find_all('p', class_ = 'lead').text


# In[11]:


soup.find('p', class_ = 'lead').text.strip()


# In[12]:


soup.find_all('th')


# In[13]:


soup.find('th').text.strip()


# In[14]:


titles = soup.find_all('th')
titles


# In[15]:


table_titles = [title.text.strip() for title in titles]
print(table_titles)


# In[16]:


import pandas as pd


# In[17]:


df = pd.DataFrame(columns = table_titles)

df


# In[18]:


column_data = soup.find_all('tr')
column_data


# In[19]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[20]:


df


# In[ ]:





# In[ ]:




