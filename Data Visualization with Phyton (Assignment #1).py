#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exploring and pre-processing a dataset using Pandas 


# In[2]:


pip install openpyxl


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


# Let's download and import our primary Canadian Immigration dataset using pandas's `read_excel()` method.


# In[5]:


df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)


# In[6]:


df_can


# In[7]:


# Replace OdName by Country as a Column Name:
df_can.rename({'OdName': 'Country'}, axis=1, inplace=True)
df_can


# In[8]:


# When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. 

# We can do this by using the `info()` method.

df_can.info()


# In[9]:


# To get the list of column headers we can call upon the data frame's `columns` instance variable.

df_can.columns


# In[10]:


# Similarly, to get the list of indices we use the `.index` instance variables.
df_can.index


# In[11]:


# Note: The default type of intance variables `index` and `columns` are NOT `list`.


# In[12]:


print(type(df_can.columns))
print(type(df_can.index))


# In[13]:


# To get the index and columns as lists, we can use the `tolist()` method.


# In[14]:


df_can.columns.tolist()
df_can.index.tolist()


# In[15]:


print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))


# In[16]:


# To view the dimensions of the dataframe, we use the `shape` instance variable of it.

# size of dataframe (rows, columns)
df_can.shape


# In[17]:


# Note: The main types stored in *pandas* objects are `float`, `int`, `bool`, `datetime64[ns]`, `datetime64[ns, tz]`, `timedelta[ns]`, `category`, and `object` (string). 

# In addition, these dtypes have item sizes, e.g. `int64` and `int32`.


# In[18]:


# Let's clean the data set to remove a few unnecessary columns. We can use *pandas* `drop()` method as follows:
df_can.drop(['AREA','REG','DEV','Type','Coverage','Unnamed: 43','Unnamed: 44','Unnamed: 45','Unnamed: 46','Unnamed: 47','Unnamed: 48','Unnamed: 49','Unnamed: 50'], axis=1, inplace=True)
df_can


# In[19]:


# We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1)
df_can['Total']


# In[20]:


# We can check to see how many null objects we have in the dataset as follows:

df_can.isnull().sum()


# In[21]:


# Finally, let's view a quick summary of each column in our dataframe using the `describe()` method.

df_can.describe()


# In[22]:


# Indexing and Selection


# In[23]:


# Select Column


# In[24]:


# Let's try filtering on the list of countries ('Country') and the data for years: 1980 - 1985.


# In[25]:


df_can.Country


# In[26]:


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]


# In[27]:


# Notice that 'Country' is string, and the years are integers. 

# for the sake of consistency, we will convert all column names to string later on.


# In[28]:


# Select Rows:

# 2 ways:    df.loc[label]    # filters by the labels of the index/column
          #  df.iloc[index]   # filters by the positions of the index/column


# In[29]:


# Notice that the default index of the dataset is a numeric range from 0 to 194. 

# This makes it very difficult to do a query by a specific country.

# This can be fixed very easily by setting the 'Country' column as the index using `set_index()` method.


# In[30]:


df_can.set_index('Country', inplace=True)


# In[31]:


df_can.head(3)


# In[32]:


# optional: to remove the name of the index
df_can.index.name = None


# In[33]:


# Filter Data: Let's view the number of immigrants from Japan (row 87) for the following scenarios:
    # 1. The full row data (all columns)
    # 2. For year 2013
    # 3. For years 1980 to 1985


# In[34]:


# 1. the full row data (all columns)
df_can.loc['Japan']


# In[35]:


# 1. alternate methods
df_can.iloc[87]


# In[36]:


# 1. alternate methods
df_can[df_can.index == 'Japan']


# In[37]:


# 2. for year 2013
df_can.loc['Japan', 2013]


# In[38]:


# 2. alternate method
# year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]


# In[39]:


# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]


# In[40]:


# 3. Alternative Method
df_can.iloc[87, [3, 4, 5, 6, 7, 8]]


# In[41]:


# Exercise

# Let's view the number of immigrants from Haiti for the following scenarios: 

# 1. The full row data (all columns) 
# 2. For year 2000 
# 3. For years 1990 to 1995


# In[45]:


# 1. the full row data (all columns)
df_can.loc['Haiti']


# In[46]:


# 2. for year 2000
df_can.loc['Haiti', 2000]


# In[47]:


#  3. for years 1990 to 1995
df_can.loc['Haiti', [1990, 1991, 1992, 1993, 1994, 1995]]


# In[48]:


# Column names that are integers (such as the years) might introduce some confusion. 

# For example, when we are referencing the year 2013, one might confuse that when the 2013th positional index. 

# To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.

df_can.columns = list(map(str, df_can.columns))


# In[50]:


# Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:

years = list(map(str, range(1980, 2014)))
years


# In[ ]:


# Exercise: Create a list named 'year' using map function for years ranging from 1990 to 2013.

# Then extract the data series from the dataframe df_can for Haiti using year list. 


# In[52]:


year = list(map(str, range(1990, 2014)))
haiti = df_can.loc['Haiti', year]
haiti


# In[53]:


# Filtering based on a criteria

# To filter the dataframe based on a condition, we simply pass the condition as a boolean vector. 


# In[54]:


# For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).


# In[56]:


# 1. create the condition boolean series
condition = df_can['AreaName'] == 'Asia'
print(condition)


# In[57]:


# 2. pass this condition into the dataFrame
df_can[condition]


# In[59]:


# We can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['AreaName']=='Asia') & (df_can['RegName']=='Southern Asia')]

# Note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# Don't forget to enclose the two conditions in parentheses


# In[60]:


# Exercise:Fetch the data where AreaName is 'Africa' and RegName is 'Southern Africa'. 

# Display the dataframe and find out how many instances are there?


# In[61]:


df_can[(df_can['AreaName']=='Africa') & (df_can['RegName']=='Southern Africa')]


# In[62]:


# Sorting Values of a Dataframe or Series

# You can use the `sort_values()` function is used to sort a DataFrame or a Series based on one or more columns. 

# You to specify the column(s) by which you want to sort and the order (ascending or descending).


# In[63]:


# Let's sort out dataframe df_can on 'Total' column

# Descending order to find out the top 5 countries that contributed the most to immigration to Canada. 

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5


# In[64]:


# Exercise: Find out top 3 countries that contributes the most to immigration to Canda in the year 2010.

# Display the country names with the immigrant count in this year


# In[65]:


df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top3_2010 = df_can['2010'].head(3)
top3_2010

