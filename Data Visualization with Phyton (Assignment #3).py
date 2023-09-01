#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Area Plots, Histograms, Bar Charts, Pie Charts, Box Plots, Scatter Plots, and Bubble Plots


# In[2]:


import numpy as np  
import pandas as pd 

# use the inline backend to generate the plots within the browser
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')  # optional: for ggplot-like style


# In[3]:


df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')


# In[4]:


df_can.head()


# In[5]:


print(df_can.shape)


# In[6]:


df_can.set_index('Country', inplace=True)


# In[7]:


# finally, let's create a list of years from 1980 - 2013
# this will come in handy when we start plotting the data

years = list(map(str, range(1980, 2014)))
years


# In[8]:


# Area Plots


# In[9]:


df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head()

# transpose the dataframe
df_top5 = df_top5[years].transpose()

df_top5.head()


# In[10]:


# Area plots are stacked by default.

# To produce a stacked area plot, each column must be either all positive or all negative values (any `NaN`, i.e. not a number, values will default to 0). 

# To produce an unstacked plot, set parameter `stacked` to value `False`.


# In[11]:


# let's change the index values of df_top5 to type integer for plotting

df_top5.index = df_top5.index.map(int)

df_top5.plot(kind='area',
             stacked=False,
             figsize=(20, 10))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[12]:


# The unstacked plot has a default transparency (alpha value) at 0.5. 

# We can modify this value by passing in the `alpha` parameter.


# In[13]:


df_top5.plot(kind='area', 
             alpha=0.25,             # 0 - 1, default value alpha = 0.5
             stacked=False,
             figsize=(20, 10))

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[14]:


# Two Types of Plotting with Matplotlib

    # Option 1: Scripting layer (procedural method) - using matplotlib.pyplot as 'plt' (what we have been using so far)
    
    
    # Option 2: Artist layer (Object oriented method) - using an `Axes` instance from Matplotlib (preferred)
        
        # This option sometimes is more transparent and flexible to use for advanced plots
        # (in particular when having multiple plots, as you will see later).


# In[15]:


# Option 1: Scripting layer

df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10)) 
plt.title('Immigration trend of top 5 countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()


# In[16]:


# Option 2: Artist layer

ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10))

ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')


# In[17]:


# Question 1: Use the scripting layer to create a stacked area plot of the 5 countries that contributed the least to immigration to Canada from 1980 to 2013. 

# Use a transparency value of 0.45.


# In[18]:


# get the 5 countries with the least contribution
df_least5 = df_can.tail(5)
     
# transpose the dataframe
df_least5 = df_least5[years].transpose() 
df_least5.head()

df_least5.index = df_least5.index.map(int) # let's change the index values of df_least5 to type integer for plotting
df_least5.plot(kind='area', alpha=0.45, figsize=(20, 10)) 

plt.title('Immigration Trend of 5 Countries with Least Contribution to Immigration')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# In[19]:


# Question 2: Use the artist layer to create an unstacked area plot of the 5 countries that contributed the least to immigration to Canada from 1980 to 2013. 
    
# Use a transparency value of 0.55.


# In[20]:


# get the 5 countries with the least contribution
df_least5 = df_can.tail(5)

# transpose the dataframe
df_least5 = df_least5[years].transpose() 
df_least5.head()

df_least5.index = df_least5.index.map(int) # let's change the index values of df_least5 to type integer for plotting
    
ax = df_least5.plot(kind='area', alpha=0.55, stacked=False, figsize=(20, 10))
    
ax.set_title('Immigration Trend of 5 Countries with Least Contribution to Immigration')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')


# In[21]:


# Histograms


# In[22]:


# Question: What is the frequency distribution of the number (population) of new immigrants 
#           from the various countries to Canada in 2013?


# In[23]:


# Before we proceed with creating the histogram plot, let's first examine the data split into intervals. 

# To do this, we will us **Numpy**'s `histrogram` method to get the bin ranges and frequency counts


# In[24]:


# let's quickly view the 2013 data
df_can['2013'].head()


# In[25]:


count, bin_edges = np.histogram(df_can['2013'])


# In[26]:


# np.histogram returns 2 values

print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins


# In[27]:


# 178 countries contributed between 0 to 3412.9 immigrants
# 11 countries contributed between 3412.9 to 6825.8 immigrants
# 1 country contributed between 6285.8 to 10238.7 immigrants, and so on..


# In[28]:


df_can['2013'].plot(kind='hist', figsize=(8, 5))

plt.title('Histogram of Immigration from 195 Countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrants')

plt.show()


# In[29]:


# Notice that the x-axis labels do not match with the bin size. 

# This can be fixed by passing in a `xticks` keyword that contains the list of the bin sizes


# In[30]:


# 'bin_edges' is a list of bin intervals

count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)

plt.title('Histogram of Immigration from 195 countries in 2013')
plt.ylabel('Number of Countries') 
plt.xlabel('Number of Immigrants')

plt.show()


# In[31]:


# We can also plot multiple histograms on the same plot. 

# For example, let's try to answer the following questions using a histogram.

# Question 3: What is the immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013?


# In[32]:


df_can.loc[['Denmark', 'Norway', 'Sweden'], years]


# In[33]:


df_can.loc[['Denmark', 'Norway', 'Sweden'], years].plot.hist()


# In[34]:


# That does not look right!

# Don't worry, you'll often come across situations like this when creating plots. 

# The solution often lies in how the underlying dataset is structured.

# Instead of plotting the population frequency distribution of the population for the 3 countries, pandas instead plotted the population frequency distribution for the `years`.

# This can be easily fixed by first transposing the dataset


# In[35]:


# transpose dataframe
df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_t.head()


# In[36]:


# generate histogram
df_t.plot(kind='hist', figsize=(10, 6))

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()


# In[37]:


# Let's make a few modifications to improve the impact and aesthetics of the previous plot:

#   increase the bin size to 15 by passing in `bins` parameter;
#   set transparency to 60% by passing in `alpha` parameter;
#   label the x-axis by passing in `x-label` parameter;
#   change the colors of the plots by passing in `color` parameter.


# In[38]:


# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)

# un-stacked histogram
df_t.plot(kind ='hist', 
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen']
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()


# In[39]:


# Tip: For a full listing of colors available in Matplotlib, run the following code in your python shell

import matplotlib
for name, hex in matplotlib.colors.cnames.items():
    print(name, hex)


# In[40]:


# If we do not want the plots to overlap each other, we can stack them using the `stacked` parameter. 

# Let's also adjust the min and max x-axis labels to remove the extra gap on the edges of the plot. 
# We can pass a tuple (min,max) using the `xlim` paramater.


# In[41]:


count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes 
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

# stacked Histogram
df_t.plot(kind='hist',
          figsize=(10, 6), 
          bins=15,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen'],
          stacked=True,
          xlim=(xmin, xmax)
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants') 

plt.show()


# In[42]:


# Question 4: Use the scripting layer to display the immigration distribution for Greece, Albania, and Bulgaria for years 1980 - 2013? 

# Use an overlapping plot with 15 bins and a transparency value of 0.35.


# In[43]:


# create a dataframe of the countries of interest (cof)
df_cof = df_can.loc[['Greece', 'Albania', 'Bulgaria'], years]


# In[44]:


# transpose the dataframe
df_cof = df_cof.transpose()


# In[45]:


# let's get the x-tick values
count, bin_edges = np.histogram(df_cof, 15)


# In[46]:


# Un-stacked Histogram
df_cof.plot(kind ='hist',
            figsize=(10, 6),
            bins=15,
            alpha=0.35,
            xticks=bin_edges,
            color=['coral', 'darkslateblue', 'mediumseagreen']
                )

plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()


# In[47]:


# Bar Charts


# In[48]:


# Question: Let's compare the number of Icelandic immigrants (country = 'Iceland') to Canada from year 1980 to 2013.


# In[49]:


# step 1: get the data
df_iceland = df_can.loc['Iceland', years]
df_iceland.head()


# In[50]:


# step 2: plot data
df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year') 
plt.ylabel('Number of immigrants') 
plt.title('Icelandic immigrants to Canada from 1980 to 2013') 

plt.show()


# In[51]:


# Impact of the financial crisis: the number of immigrants to Canada started increasing rapidly after 2008.


# In[52]:


# Let's annotate this on the plot using the `annotate` method of the scripting layer or the pyplot interface. 

# We will pass in the following parameters:

    # `s`: str, the text of annotation.
    # `xy`: Tuple specifying the (x,y) point to annotate (in this case, end point of arrow).
    # `xytext`: Tuple specifying the (x,y) point to place the text (in this case, start point of arrow).
    # `xycoords`: The coordinate system that xy is given in - 'data' uses the coordinate system of the object being annotated (default).
    # `arrowprops`: Takes a dictionary of properties to draw the arrow:
    # `arrowstyle`: Specifies the arrow style, `'->'` is standard arrow.
    # `connectionstyle`: Specifies the connection type. `arc3` is a straight line.
    # `color`: Specifies color of arrow.
    # `lw`: Specifies the line width.


# In[53]:


df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)  # rotate the xticks(labelled points on x-axis) by 90 degrees

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',  # s: str. Will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )

plt.show()


# In[54]:


# Let's also annotate a text to go over the arrow.  We will pass in the following additional parameters:

    # `rotation`: rotation angle of text in degrees (counter clockwise)
    # `va`: vertical alignment of text \[‘center’ | ‘top’ | ‘bottom’ | ‘baseline’]
    # `ha`: horizontal alignment of text \[‘center’ | ‘right’ | ‘left’]


# In[55]:


df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',  # s: str. will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )

# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' algned.
             )

plt.show()


# In[56]:


# Question 5: Using the scripting layer and the `df_can` dataset, create a horizontal bar plot showing the total number of immigrants to Canada from the top 15 countries, for the period 1980 - 2013. 

# Label each country with the total immigrant count.


# In[57]:


# sort dataframe on 'Total' column (descending)
df_can.sort_values(by='Total', ascending=False, inplace=True)

# get top 15 countries
df_top15 = df_can['Total'].head(15)
df_top15


# In[58]:


# generate plot
df_top15.plot(kind='barh', figsize=(12, 12), color='steelblue')
plt.xlabel('Number of Immigrants')
plt.title('Top 15 Conuntries Contributing to the Immigration to Canada between 1980 - 2013')

# annotate value labels to each country
for index, value in enumerate(df_top15): 
    label = format(int(value), ',') # format int with commas
    
# place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
plt.annotate(label, xy=(value - 47000, index - 0.10), color='white')

plt.show()


# In[59]:


# Pie Charts


# In[60]:


# Step 1: Gather data.

# group countries by continents and apply sum() function 
df_continents = df_can.groupby('Continent', axis=0).sum()

# note: the output of the groupby method is a `groupby' object. 
# we can not use it further until we apply a function (eg .sum())

print(type(df_can.groupby('Continent', axis=0)))
df_continents.head()


# In[61]:


# Step 2: Plot the data. We will pass in `kind = 'pie'` keyword, along with the following additional parameters:

 # `autopct` : is a string or function used to label the wedges with their numeric value. The label will be placed inside the wedge. If it is a format string, the label will be `fmt%pct`.
 # `startangle : rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.
 #  `shadow` : Draws a shadow beneath the pie (to give a 3D feel).


# In[62]:


# autopct create %, start angle represent starting point

df_continents['Total'].plot(kind='pie',
                            figsize=(5, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=90,     # start angle 90° (Africa)
                            shadow=True,       # add shadow      
                            )

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal') # Sets the pie chart to look like a circle.
plt.legend(labels=df_continents.index, loc='upper left') 


plt.show()


# In[63]:


# The above visual is not very clear, the numbers and text overlap in some instances. 

# Let's make a few modifications to improve the visuals:

    # Remove the text labels on the pie chart by passing in `legend` and add it as a seperate legend using `plt.legend()`.
    # Push out the percentages to sit just outside the pie chart by passing in `pctdistance` parameter.
    # Pass in a custom set of colors for continents by passing in `colors` parameter.
    # Explode the pie chart to emphasize the lowest three continents (Africa, North America, and Latin America and Caribbean) 
    # by passing in `explode` parameter.


# In[64]:


colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.

df_continents['Total'].plot(kind='pie',
                            figsize=(10, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            #colors=colors_list,  # add custom colors
                            #explode=explode_list # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12, fontsize = 15) 

plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left', fontsize=7) 

plt.show()


# In[65]:


# Question 6: Using a pie chart, explore the proportion (percentage) of new immigrants grouped by continents in the year 2013.

# Note: You might need to play with the explore values in order to fix any overlapping slice values.


# In[66]:


explode_list = [0.0, 0, 0, 0.1, 0.1, 0.2] # ratio for each continent with which to offset each wedge.

df_continents['2013'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,                 # turn off labels on pie chart
                            pctdistance=1.12,            # the ratio between the pie center and start of text label
                            explode=explode_list         # 'explode' lowest 3 continents
                                )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent in 2013', y=1.12) 
plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

# show plot
plt.show()


# In[67]:


# Box Plots


# In[68]:


# Let's plot the box plot for the Japanese immigrants between 1980 - 2013.


# In[69]:


# Step 1: Get the subset of the dataset. 

# Even though we are extracting the data for just one country, we will obtain it as a dataframe. 
# This will help us with calling the `dataframe.describe()` method to view the percentiles.


# In[70]:


df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.head()


# In[71]:


# Step 2: Plot by passing in `kind='box'`.

df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()


# In[72]:


# We can view the actual numbers by calling the `describe()` method on the dataframe.

df_japan.describe()


# In[73]:


# One of the key benefits of box plots is comparing the distribution of multiple datasets.

# Question 7: Compare the distribution of the number of new immigrants from India and China for the period 1980 - 2013.


# In[74]:


# Step 1: Get the dataset for China and India and call the dataframe df_CI.

df_CI= df_can.loc[['China', 'India'], years].transpose()
df_CI.head()


# In[75]:


# Let's view the percentiles associated with both countries using the `describe()` method.
df_CI.describe()


# In[76]:


# Step 2: Plot data.
df_CI.plot(kind='box', figsize=(10, 7))

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.ylabel('Number of Immigrants')
plt.show()


# In[77]:


# If you prefer to create horizontal box plots, you can pass the `vert` parameter in the plot function and assign it to False. 

# You can also specify a different color in case you are not a big fan of the default red color.

df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')

plt.show()


# In[78]:


# Subplots


# In[79]:


# Often times we might want to plot multiple plots within the same figure. 
# For example, we might want to perform a side by side comparison of the box plot with the line plot of China and India's immigration.


    # fig = plt.figure() # create figure
    # ax = fig.add_subplot(nrows, ncols, plot_number) # create subplots


# `nrows` and `ncols` are used to notionally split the figure into (`nrows` \* `ncols`) sub-axes,
# `plot_number` is used to identify the particular subplot that this function is to create within the notional grid.
# 'plot_number` starts at 1, increments across rows first and has a maximum of `nrows` \* `ncols`


# In[80]:


# We can then specify which subplot to place each plot by passing in the `ax` paramemter in `plot()` method as follows:


# In[81]:


fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot). See tip below**

# Subplot 1: Box plot
df_CI.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0) # add to subplot 1
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Subplot 2: Line plot
df_CI.plot(kind='line', figsize=(20, 6), ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()


# In[82]:


# Tip regarding subplot convention

# In the case when `nrows`, `ncols`, and `plot_number` are all less than 10, a convenience exists such that a 3-digit number can be given instead, 
# where the hundreds represent `nrows`, the tens represent `ncols` and the units represent `plot_number`. 

# For instance,

       #  subplot(211) == subplot(2, 1, 1) 


# Produces a subaxes in a figure which represents the top plot (i.e. the first) in a 2 rows by 1 column notional grid 
# (no grid actually exists, but conceptually this is how the returned subplot has been positioned).


# In[83]:


# Previously we identified the top 15 countries based on total immigration from 1980 - 2013.

# Question: Create a box plot to visualize the distribution of the top 15 countries (based on total immigration) 
#           grouped by the decades `1980s`, `1990s`, and `2000s`.


# In[84]:


# Step 1: Get the dataset. Get the top 15 countries based on Total immigrant population. Name the dataframe df_top15.

df_top15 = df_can.sort_values(['Total'], ascending=False, axis=0).head(15)
df_top15


# In[85]:


# Step 2: Create a new dataframe which contains the aggregate for each decade. One way to do that:

    #  1.  Create a list of all years in decades 80's, 90's, and 00's.
    #  2.  Slice the original dataframe df_can to create a series for each decade and sum across all years for each country.
    #  3.  Merge the three series into a new data frame. Call your dataframe new_df.


# In[86]:


# create a list of all years in decades 80's, 90's, and 00's
years_80s = list(map(str, range(1980, 1990))) 
years_90s = list(map(str, range(1990, 2000))) 
years_00s = list(map(str, range(2000, 2010))) 

# slice the original dataframe df_can to create a series for each decade
df_80s = df_top15.loc[:, years_80s].sum(axis=1) 
df_90s = df_top15.loc[:, years_90s].sum(axis=1) 
df_00s = df_top15.loc[:, years_00s].sum(axis=1)

# merge the three series into a new data frame
new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s':df_00s}) 
new_df.head()


# In[87]:


new_df.describe()


# In[88]:


# Step 3: Plot the box plots.

new_df.plot(kind='box', figsize=(10, 6))
plt.title('Immigration from top 15 countries for decades 80s, 90s and 2000s')

plt.show()


# In[89]:


# Note how the box plot differs from the summary table created. 

# The box plot scans the data and identifies the outliers. In order to be an outlier, the data value must be:<br>

        # larger than Q3 by at least 1.5 times the interquartile range (IQR), or,
        # smaller than Q1 by at least 1.5 times the IQR.
        
# Using the definition of outlier, any value that is greater than Q3 by 1.5 times IQR will be flagged as outlier.

        #  Outlier > 105,505.5 + (1.5 \* 69,404)
        #  Outlier > 209,611.5


# In[90]:


# let's check how many entries fall above the outlier threshold 

new_df=new_df.reset_index()
new_df[new_df['2000s']> 209611.5]


# In[91]:


# China and India are both considered as outliers since their population for the decade exceeds 209.611,5.


# In[92]:


# Scatter Plots


# In[93]:


# let's visualize the trend of total immigrantion to Canada (all countries combined) for the years 1980 - 2013.


# In[94]:


# Step 1: Get the dataset. 

# Since we are expecting to use the relationship betewen `years` and `total population`, we will convert `years` to `int` type.


# In[95]:


# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()


# In[96]:


# Step 2: Plot the data.

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

plt.show()


# In[97]:


# The scatter plot does not connect the data points together. 

# We can clearly observe an upward trend in the data: as the years go by, the total number of immigrants increases. 

# We can mathematically analyze this upward trend using a regression line (line of best fit).


# In[98]:


# let's try to plot a linear line of best fit, and use it to  predict the number of immigrants in 2015.

    # Step 1: Get the equation of line of best fit. We will use **Numpy**'s `polyfit()` method by passing in the following:

   # `x`: x-coordinates of the data.
   # `y`: y-coordinates of the data.
   # `deg`: Degree of fitting polynomial. 1 = linear, 2 = quadratic, and so on.

x = df_tot['year']      # year on x-axis
y = df_tot['total']     # total on y-axis
fit = np.polyfit(x, y, deg=1)

fit


# In[99]:


# The output is an array with the polynomial coefficients, highest powers first
# In this case, slope in position 0 and intercept in position 1.


# In[100]:


# Step 2: Plot the regression line on the `scatter plot`.

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# print out the line of best fit
'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1]) 


# In[101]:


# Using the equation of line of best fit, we can estimate the number of immigrants in 2015

# No. Immigrants = 5567 * Year - 10926195
# No. Immigrants = 5567 * 2015 - 10926195
# No. Immigrants = 291,310


# In[102]:


# Question 8: Create a scatter plot of the total immigration from Denmark, Norway, and Sweden to Canada from 1980 to 2013


# In[103]:


# Step 1: Get the data

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

    # show resulting dataframe
df_total.head()


# In[104]:


# Step 2: Generate the scatter plot by plotting the total versus year in df_total.

    # generate scatter plot
df_total.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

    # add title and label to axes
plt.title('Immigration from Denmark, Norway, and Sweden to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

    # show plot
plt.show()


# In[105]:


# Bubble Plots

# A `bubble plot` is a variation of the `scatter plot` that displays three dimensions of data (x, y, z).


# In[106]:


# Let's start by analyzing the effect of Argentina's great depression


# In[107]:


# Let's analyze the effect of this crisis, and compare Argentina's immigration to that of it's neighbour Brazil. 

# Let's do that using a `bubble plot` of immigration from Brazil and Argentina for the years 1980 - 2013. 

# We will set the weights for the bubble as the normalized value of the population for each year.


# In[108]:


# Step 1: Get the data for Brazil and Argentina. 

# Like in the previous example, we will convert the `Years` to type int and include it in the dataframe.

# transposed dataframe
df_can_t = df_can[years].transpose()

# cast the Years (the index) to type int
df_can_t.index = map(int, df_can_t.index)

# let's label the index. This will automatically be the column name when we reset the index
df_can_t.index.name = 'Year'

# reset index to bring the Year in as a column
df_can_t.reset_index(inplace=True)

# view the changes
df_can_t.head()


# In[109]:


# Step 2: Create the normalized weights.

# normalize Brazil data
norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())

# normalize Argentina data
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())


# In[110]:


# Step 3: Plot the data

# To plot two different scatter plots in one plot, we can include the axes one plot into the other by passing it via the `ax` parameter.

# We will also pass in the weights using the `s` parameter. 

# Given that the normalized weights are between 0-1, they won't be visible on the plot. Therefore, we will:
    
    # multiply weights by 2000 to scale it up on the graph, and,
    # add 10 to compensate for the min value (which has a 0 weight and therefore scale with multiplying by 2000).


# In[111]:


# Brazil
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    figsize=(14, 8),
                    alpha=0.5,  # transparency
                    color='green',
                    s=norm_brazil * 2000 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                    )

# Argentina
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.5,
                    color="blue",
                    s=norm_argentina * 2000 + 10,
                    ax=ax0
                    )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 to 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')


# In[112]:


# The size of the bubble corresponds to the magnitude of immigrating population for that year, compared to the 1980 - 2013 data.

# We can see a corresponding increase in immigration from Argentina during the 1998 - 2002 great depression. 
# We can also observe a similar spike around 1985 to 1993.


# In[113]:


# Question 11: Create bubble plots of immigration from China and India to visualize any differences with time from 1980 to 2013.
# You can use df_can_t that we defined and used in the previous example.


# In[114]:


# Step 1: Normalize the data pertaining to China and India.

# normalized Chinese data
norm_china = (df_can_t['China'] - df_can_t['China'].min()) / (df_can_t['China'].max() - df_can_t['China'].min())
    
# normalized Indian data
norm_india = (df_can_t['India'] - df_can_t['India'].min()) / (df_can_t['India'].max() - df_can_t['India'].min())


# In[115]:


# Step 2: Generate the bubble plots.

# China
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='China',
                    figsize=(14, 8),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_china * 2000 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                       )

# India
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='India',
                    alpha=0.5,
                    color="blue",
                    s=norm_india * 2000 + 10,
                    ax = ax0
                       )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from China and India from 1980 - 2013')
ax0.legend(['China', 'India'], loc='upper left', fontsize='x-large')


# In[ ]:




