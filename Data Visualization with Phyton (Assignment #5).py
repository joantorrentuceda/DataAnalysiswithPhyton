#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Waffle Charts, Word Clouds, and Regression Plots


# In[2]:


import pandas as pd
import numpy as np
from PIL import Image # converting images into arrays


# In[3]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches # needed for waffle Charts
mpl.style.use('ggplot') # optional: for ggplot-like style
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#import wordcloud
import wordcloud


# In[5]:


df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
df_can.head()


# In[6]:


# print the dimensions of the dataframe
print(df_can.shape)


# In[7]:


#set Country as index
df_can.set_index('Country', inplace=True)


# In[8]:


# Waffle Charts


# In[9]:


# Let's revisit the previous case study about Denmark, Norway, and Sweden.

# let's create a new dataframe for these three countries 
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]

# let's take a look at our dataframe
df_dsn


# In[10]:


# Unfortunately, `waffle` charts are not built into any of the Python visualization libraries. 

# Therefore, we will learn how to create them from scratch.


# In[11]:


# Step 1: Determing the proportion of each category with respect to the total.

total_values = df_dsn['Total'].sum()
category_proportions = df_dsn['Total'] / total_values

# print out proportions
pd.DataFrame({"Category Proportion": category_proportions})


# In[12]:


# Step 2: Defining the overall size of the `waffle` chart.

width = 40 # width of chart
height = 10 # height of chart

total_num_tiles = width * height # total number of tiles

print(f'Total number of tiles is {total_num_tiles}.')


# In[13]:


# Step 3: Using the proportion of each category to determe it respective number of tiles

# compute the number of tiles for each category
tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)

# print out number of tiles per category
pd.DataFrame({"Number of tiles": tiles_per_category})


# In[14]:


# Step 4: Creating a matrix that resembles the `waffle` chart and populating it.

# initialize the waffle chart as an empty matrix
waffle_chart = np.zeros((height, width), dtype = np.uint)

# define indices to loop through waffle chart
category_index = 0
tile_index = 0

# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1       
            
        # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index
        
print ('Waffle chart populated!')


# In[15]:


# Let's take a peek at how the matrix looks like:

waffle_chart


# In[16]:


# As expected, the matrix consists of three categories. 
# The total number of each category's instances matches the total number of tiles allocated to each category.


# In[17]:


# Step 5: Map the `waffle` chart matrix into a visual.

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()
plt.show()


# In[18]:


# Step 6: Prettify the chart.

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])
plt.show()


# In[19]:


# Step 7: Create a legend and add it to chart.

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])

# compute cumulative sum of individual categories to match color schemes between chart and legend
values_cumsum = np.cumsum(df_dsn['Total'])
total_values = values_cumsum[len(values_cumsum) - 1]

# create legend
legend_handles = []
for i, category in enumerate(df_dsn.index.values):
    label_str = category + ' (' + str(df_dsn['Total'][i]) + ')'
    color_val = colormap(float(values_cumsum[i])/total_values)
    legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

# add legend to chart
plt.legend(handles=legend_handles,
           loc='lower center', 
           ncol=len(df_dsn.index.values),
           bbox_to_anchor=(0., -0.2, 0.95, .1)
          )
plt.show()


# In[20]:


# It would very inefficient to repeat these seven steps every time we wish to create a `waffle` chart. 

# So let's combine all seven steps into one function called create_waffle_chart. 

    # This function would take the following parameters as input:

        # 1.  categories: Unique categories or classes in dataframe.
        # 2.  values: Values corresponding to categories or classes.
        # 3.  height: Defined height of waffle chart.
        # 4.  width: Defined width of waffle chart.
        # 5.  colormap: Colormap class
        # 6.  value_sign: In order to make our function more generalizable, we will add this parameter to address signs 
            # that could be associated with a value such as %, $, and so on. **value_sign** has a default value of empty string.


# In[21]:


def create_waffle_chart(categories, values, height, width, colormap, value_sign=''):

    # compute the proportion of each category with respect to the total
    total_values = sum(values)
    category_proportions = [(float(value) / total_values) for value in values]

    # compute the total number of tiles
    total_num_tiles = width * height # total number of tiles
    print ('Total number of tiles is', total_num_tiles)
    
    # compute the number of tiles for each catagory
    tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

    # print out number of tiles per category
    for i, tiles in enumerate(tiles_per_category):
        print (df_dsn.index.values[i] + ': ' + str(tiles))
    
    # initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height, width))

    # define indices to loop through waffle chart
    category_index = 0
    tile_index = 0

    # populate the waffle chart
    for col in range(width):
        for row in range(height):
            tile_index += 1

            # if the number of tiles populated for the current category 
            # is equal to its corresponding allocated tiles...
            if tile_index > sum(tiles_per_category[0:category_index]):
                # ...proceed to the next category
                category_index += 1       
            
            # set the class value to an integer, which increases with class
            waffle_chart[row, col] = category_index
    
    # instantiate a new figure object
    fig = plt.figure()

    # use matshow to display the waffle chart
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart, cmap=colormap)
    plt.colorbar()

    # get the axis
    ax = plt.gca()

    # set minor ticks
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
    # add dridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    plt.xticks([])
    plt.yticks([])

    # compute cumulative sum of individual categories to match color schemes between chart and legend
    values_cumsum = np.cumsum(values)
    total_values = values_cumsum[len(values_cumsum) - 1]

    # create legend
    legend_handles = []
    for i, category in enumerate(categories):
        if value_sign == '%':
            label_str = category + ' (' + str(values[i]) + value_sign + ')'
        else:
            label_str = category + ' (' + value_sign + str(values[i]) + ')'
            
        color_val = colormap(float(values_cumsum[i])/total_values)
        legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

    # add legend to chart
    plt.legend(
        handles=legend_handles,
        loc='lower center', 
        ncol=len(categories),
        bbox_to_anchor=(0., -0.2, 0.95, .1)
    )
    plt.show()


# In[22]:


# Now to create a `waffle` chart, all we have to do is call the function `create_waffle_chart`.

width = 40 # width of chart
height = 10 # height of chart

categories = df_dsn.index.values # categories
values = df_dsn['Total'] # correponding values of categories

colormap = plt.cm.coolwarm # color map class

create_waffle_chart(categories, values, height, width, colormap)


# In[23]:


# New Python package for generating `waffle charts` called [PyWaffle]

#install pywaffle
get_ipython().system('pip install pywaffle')

#import Waffle from pywaffle
from pywaffle import Waffle

#Set up the Waffle chart figure

fig = plt.figure(FigureClass = Waffle,
                 rows = 20, columns = 30, #pass the number of rows and columns for the waffle 
                 values = df_dsn['Total'], #pass the data to be used for display
                 cmap_name = 'tab20', #color scheme
                 legend = {'labels': [f"{k} ({v})" for k, v in zip(df_dsn.index.values,df_dsn.Total)],
                            'loc': 'lower left', 'bbox_to_anchor':(0,-0.1),'ncol': 3}
                 #notice the use of list comprehension for creating labels 
                 #from index and total of the dataset
                )

#Display the waffle chart
plt.show()


# In[24]:


# Question 1:  Create a Waffle chart to display the proportions of China and India total immigrant contribution.

data_CI= df_can.loc[['China', 'India'], :]
data_CI
                    


# In[25]:


fig = plt.figure(FigureClass = Waffle,
                 rows = 20, columns = 30, #pass the number of rows and columns for the waffle 
                 values = data_CI['Total'], #pass the data to be used for display
                 cmap_name = 'tab20', #color scheme
                 legend = {'labels': [f"{k} ({v})" for k, v in zip(data_CI.index.values,data_CI.Total)],
                            'loc': 'lower left', 'bbox_to_anchor':(0,-0.1),'ncol': 3}
                 #notice the use of list comprehension for creating labels 
                 #from index and total of the dataset
                )

#Display the waffle chart
plt.show()


# In[26]:


# Word Clouds


# In[27]:


from wordcloud import WordCloud

print ('Wordcloud imported!')


# In[28]:


# Let's generate sample text data from our immigration dataset, say text data of 90 words.


# In[29]:


# What was the total immigration from 1980 to 2013?

total_immigration = df_can['Total'].sum()
total_immigration


# In[30]:


# Using countries with single-word names, 
# let's duplicate each country's name based on how much they contribute to the total immigration.

max_words = 90
word_string = ''
for country in df_can.index.values:
     # check if country's name is a single-word name
    if country.count(" ") == 0:
        repeat_num_times = int(df_can.loc[country, 'Total'] / total_immigration * max_words)
        word_string = word_string + ((country + ' ') * repeat_num_times)

# display the generated text
word_string


# In[31]:


get_ipython().run_line_magic('pip', 'install --upgrade Pillow')
get_ipython().run_line_magic('pip', 'install --upgrade numpy')


# In[32]:


# create the word cloud
wordcloud = WordCloud(background_color='white').generate(word_string)

print('Word cloud created!')


# In[33]:


# display the cloud
plt.figure(figsize=(14, 18))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[34]:


# Plotting with Seaborn


# In[35]:


df_can['Continent'].unique()


# In[36]:


# countplot

# Let's find the count of Continents in the data 'df_can' using countplot on 'Continent'

sns.countplot(x='Continent', data=df_can)


# In[37]:


# The labels on the x-axis doesnot look as expected. 

# Let's try to replace: 
    
    # 'Latin America and the Caribbean' with and "L-America", 
    # 'Northern America' with "N-America", 
    # Change the figure size and then display the plot again
    


# In[38]:


df_can1 = df_can.replace('Latin America and the Caribbean', 'L-America')
df_can1 = df_can1.replace('Northern America', 'N-America')


# In[39]:


plt.figure(figsize=(15, 10))
sns.countplot(x='Continent', data=df_can1)


# In[40]:


# Barplot

# This plot will perform the Groupby on a categorical varaible and plot aggregated values, with confidence intervals.

# Let's plot the total immigrants Continent-wise


# In[41]:


plt.figure(figsize=(15, 10))
sns.barplot(x='Continent', y='Total', data=df_can1)


# In[42]:


# You can verify the values by performing the groupby on the Total and Continent for mean()

df_Can2=df_can1.groupby('Continent')['Total'].mean()
df_Can2


# In[43]:


# Regression Plot


# In[44]:


years = list(map(str, range(1980, 2014)))

# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()


# In[45]:


sns.regplot(x='year', y='total', data=df_tot)


# In[46]:


# Let's change the color to green.

sns.regplot(x='year', y='total', data=df_tot, color='green')
plt.show()


# In[47]:


# Customize the marker shape, so instead of circular markers, let's use `+`.

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+')
plt.show()


# In[48]:


# Let's blow up the plot a little so that it is more appealing to the sight.

plt.figure(figsize=(15, 10))
sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+')
plt.show()


# In[49]:


# Let's increase the size of markers so they match the new size of the figure, and add a title and x- and y-labels.

plt.figure(figsize=(15, 10))
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})

ax.set(xlabel='Year', ylabel='Total Immigration') # add x- and y-labels
ax.set_title('Total Immigration to Canada from 1980 - 2013') # add title
plt.show()


# In[50]:


# finally increase the font size of the tickmark labels, the title, and the x- and y-labels so they don't feel left out!

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()


# In[51]:


# If you are not a big fan of the purple background, you can easily change the style to a white plain background.

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)
sns.set_style('ticks')  # change background to white background

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()


# In[52]:


# Or to a white background with gridlines.

plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)
sns.set_style('whitegrid')

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()


# In[53]:


# Question 2: Use seaborn to create a scatter plot with a regression line to visualize the total immigration 
# from Denmark, Sweden, and Norway to Canada from 1980 to 2013.


# In[54]:


# create df_countries dataframe
df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

# create df_total by summing across three countries for each year
df_total = pd.DataFrame(df_countries.sum(axis=1))

# reset index in place
df_total.reset_index(inplace=True)

# rename columns
df_total.columns = ['year', 'total']

# change column year from string to int to create scatter plot
df_total['year'] = df_total['year'].astype(int)

# define figure size
plt.figure(figsize=(15, 10))

# define background style and font size
sns.set(font_scale=1.5)
sns.set_style('whitegrid')

# generate plot and add title and axes labels
ax = sns.regplot(x='year', y='total', data=df_total, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigrationn from Denmark, Sweden, and Norway to Canada from 1980 - 2013')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




