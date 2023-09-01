#!/usr/bin/env python
# coding: utf-8

# # Data Scraping using Phyton (Project)

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


soup.find('table')


# In[5]:


# The second table of the website is our table of interest, we find it looking for position 1 in the list of tables:

soup.find_all('table')[1]


# In[6]:


# Another option is using 'find' and class attribute to look for the table of interest.
# We know that our table is the first of the class 'wikitable sortable'

soup.find('table', class_ = 'wikitable sortable')


# In[7]:


# We define our table, as table variable:

table = soup.find_all('table')[1]


# In[8]:


# From our table we look for attribute 'th' to extract the titles

titles = table.find_all('th')
titles


# In[9]:


# Then, we use a loop to extract a list of the titles and include them into the dataframe
table_titles = [title.text.strip() for title in titles]
print(table_titles)


# In[10]:


import pandas as pd


# In[11]:


df = pd.DataFrame(columns = table_titles)

df


# In[12]:


# Now we need to obtain our data, that is, each row of the table.

# From our table we look for attribute 'tr' to extract the rows

column_data = table.find_all('tr')


# In[13]:


# Then, we use a loop to extract a list of the rows and append them into the dataframe

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[14]:


df


# In[17]:


# Finally, we convert the dataframe into a csv
df.to_csv(r'C:\Users\joant\Documents\PERS\Cursos Data Analysis\Data Analysis with Phyton\TopCompanies.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




