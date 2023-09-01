#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create visualizations using Matplotib, Seaborn and Folium


# In[2]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium


# In[3]:


# Importing Data

df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')
print('Data downloaded and read into a dataframe!')


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


# TASK 1.1: Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year


# In[9]:


df_new=df.groupby('Year')['Automobile_Sales'].mean()
df_new


# In[10]:


plt.figure(figsize=(10, 6))
df_new.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Automobile Sales over Time')
plt.show()


# In[11]:


years= list(range(1980,2024))


# In[12]:


plt.figure(figsize=(14, 8))
df_new.plot(kind='line')
plt.xticks(years, rotation=80)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Automobile Sales during Recession')
plt.text(2005, 2000, '2007 Recession')
plt.text(1990, 2000, '1991 Recession')
plt.legend()
plt.show()


# In[13]:


# TASK 1.2: Plot different lines for categories of vehicle type and analyse the trend to answer the question. 

# Is there a noticeable difference in sales trends between different vehicle types during recession periods?


# In[14]:


df_new = df.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()
df_new


# In[15]:


df_new.set_index('Year', inplace=True)
df_new.head()


# In[16]:


df_new = df_new.groupby(['Vehicle_Type'])['Automobile_Sales']
df_new.head()


# In[17]:


plt.figure(figsize=(14, 8))
df_new.plot(kind='line')
plt.xticks(years, rotation=80)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Trend Vehicle-wise during Recession')
plt.legend()
plt.show()


# In[18]:


# In recession periods the sales trends differ across different vehicle types. While superminicar and smallfamilycar perform
# relatively well in terms of sales, Sport type vehicles decrease sales because of the high cost of the vehicle. 


# In[19]:


# TASK 1.3: Use the functionality of Seaborn Library. 

# Create a visualization to compare the sales trend per vehicle type for a recession period with a non-recession period.


# In[20]:


new_df2 = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
new_df2


# In[21]:


plt.figure(figsize=(14, 8))
sns.barplot(data=new_df2, x='Recession', y='Automobile_Sales', hue='Recession')
plt.xlabel('')
plt.ylabel('Average Automobile Sales')
plt.title('Average Automobile Sales during Recession and Non-Recession')
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.show()


# In[22]:


# Compare the sales of different vehicle types during a recession and a non-recession period


# In[23]:


new_df3 = df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
new_df3


# In[24]:


# We need only the recession periods (that is, Recession = 1)
recession_data = df[df['Recession'] == 1]
recession_data


# In[25]:


# We need only the non-recession periods (that is, Recession = 0)
non_recession_data= df[df['Recession'] == 0]
non_recession_data


# In[26]:


# Calculate the total sales volume by vehicle type during recessions

sales_by_vehicle_type = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
sales_by_vehicle_type


# In[27]:


# Calculate the total sales volume by vehicle type during non-recessions
sales_by_vehicle_type2 = non_recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
sales_by_vehicle_type2


# In[28]:


# Create the grouped bar chart using seaborn
plt.figure(figsize=(14, 8))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=new_df3)
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
plt.xlabel('Period')
plt.ylabel('Average Automobile Sales')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
plt.show()


# In[29]:


# Generalized decline in overall vehicle sales during recessions. Sports and Executive Car are the most affected vehicle types.


# In[30]:


# TASK 1.4: Use sub plotting to compare the variations in GDP during recession and non-recession period. 

# Develop line plots for each period.


# In[31]:


recession_data = df[df['Recession'] == 1]
non_recession_data= df[df['Recession'] == 0]


# In[32]:


fig=plt.figure(figsize=(14, 8))
    
#Create different axes for subploting
ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot). 

# Subplot 1
sns.lineplot(x='Year', y='GDP', data=recession_data, label='Recession',ax=ax0)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation during Recession Period')

# Subplot 2
sns.lineplot(x='Year', y='GDP', data=non_recession_data, label='Non-Recession',ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP')
ax1.set_title('GDP Variation during Non-Recession Period')
    
plt.tight_layout()
plt.show()


# In[33]:


# During recessions, we observe a lower level of GDP. This could be a possible explanation of the generalized decrease in sales.


# In[34]:


# TASK 1.5: Develop a Bubble plot for displaying the impact of seasonality on Automobile Sales.


# In[35]:


size=non_recession_data['Seasonality_Weight']


# In[36]:


fig=plt.figure(figsize=(14, 8))
sns.scatterplot(data=non_recession_data, x='Month', y='Automobile_Sales', size=size, hue='Seasonality_Weight', legend=True)
plt.xlabel('Month')
plt.ylabel('Automobile_Sales')
plt.title('Seasonality impact on Automobile Sales')

plt.show()


# In[37]:


# Seasonality has not affected on the overall sales. However, there is a drastic raise in sales in the month of April


# In[38]:


# TASK 1.6: Use the functionality of Matplotlib to develop a scatter plot to identify the correlation between average vehicle 
#           price relate to the sales volume during recessions.


# From the data, develop a scatter plot to identify if there a correlation between consumer confidence and automobile sales 
# during recession period? 


# In[39]:


fig=plt.figure(figsize=(14, 8))
recession_data = df[df['Recession'] == 1]
plt.scatter(recession_data['Price'], recession_data['Automobile_Sales'])
plt.xlabel('Price')
plt.ylabel('Automobile_Sales')
plt.title('Correlation between average vehicle price and automobile sales during recession period')
plt.show()


# In[40]:


fig=plt.figure(figsize=(14, 8))
recession_data = df[df['Recession'] == 1]
plt.scatter(recession_data['Consumer_Confidence'], recession_data['Automobile_Sales'])
plt.xlabel('Consumer_Confidence')
plt.ylabel('Automobile_Sales')
plt.title('Correlation between consumer confidence and automobile sales during recession period')
plt.show()


# In[41]:


# There is not much relation!


# In[42]:


# TASK 1.7: Create a pie chart to display the portion of advertising expenditure of XYZAutomotives 
# during recession and non-recession periods.


# In[43]:


recession_data = df[df['Recession'] == 1]
non_recession_data= df[df['Recession'] == 0]


# In[44]:


# Total Advertising expenditure for Recessions and Non-Recession periods
TAd_r = recession_data['Advertising_Expenditure'].sum()
TAd_Nr = non_recession_data['Advertising_Expenditure'].sum()


# In[45]:


fig=plt.figure(figsize=(14, 8))
plt.pie([TAd_r, TAd_Nr], labels=['Recession', 'Non-Recession'], autopct='%1.1f%%')
plt.title('Advertising Expenditure during Recession and Non-Recession Periods')

plt.show()


# In[46]:


# Advertisements during non-recession periods exceeds by far advertisements during recession times.


# In[47]:


# TASK 1.8: Develop a pie chart to display the total Advertisement expenditure for each vehicle type during recession period.

# Can we observe the share of each vehicle type in total sales during recessions? 

# Create another pie plot to display the total advertisement expenditure for each vehicle type


# In[48]:


recession_data = df[df['Recession'] == 1]


# In[49]:


# Total Ad Expenditure per Vehicle Type during Recessions
TAvr = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
TAvr


# In[50]:


TAvr.index


# In[51]:


TAvr.values


# In[52]:


fig=plt.figure(figsize=(14, 8))
labels = TAvr.index
sizes = TAvr.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Share of Each Vehicle Type in Total Advertising Expenditure during Recessions')

plt.show()


# In[53]:


# In recession periods, the advertisement expenditure is highly concentrated in relatively low-price vehicles. 
# Sports and Executive Cars (High-Price) have relatively low advertisement expenditure.


# In[54]:


# Total Sales per Vehicle Type during Recessions
TSvr = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum()
TSvr


# In[55]:


fig=plt.figure(figsize=(14, 8))
labels = TSvr.index
sizes = TSvr.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Share of Each Vehicle Type in Total Sales during Recessions')

plt.show()


# In[56]:


# Look at this! In terms of sales during recessions, the distribution is very similar to what we obtained in terms of Adds.


# In[57]:


# TASK 1.9: Develop a countplot to analyse the effect of the unemployment rate on vehicle type and sales 
#            during the Recession Period.


# In[58]:


recession_data = df[df['Recession'] == 1]


# In[59]:


fig=plt.figure(figsize=(14, 8))
sns.countplot(data=recession_data, x='unemployment_rate', hue='Vehicle_Type')
plt.xlabel('Unemployment Rate')
plt.ylabel('Count')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales during Recessions')
plt.legend(loc='upper right')
plt.show()


# In[60]:


fig=plt.figure(figsize=(14, 8))
sns.countplot(data=non_recession_data, x='unemployment_rate', hue='Vehicle_Type')
plt.xlabel('Unemployment Rate')
plt.ylabel('Count')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales during Non-Recessions')
plt.legend(loc='upper right')
plt.show()


# In[61]:


# If we compare the effect of unemployment (recession measure) on vehicle type and sales, we can observe that even sales

# decrease for all types of vehicles when the recession comes, the low-range ones are more robust and suffers less than 

# the high-range in terms of sales. 


# In[62]:


# OPTIONAL : TASK 1.10 Create a map on the hightest sales region/offices of the company during recession period


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




