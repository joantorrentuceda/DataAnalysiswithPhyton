#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating maps and visualizing Geospatial data


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


get_ipython().system('pip3 install folium==0.5.0')
import folium

print('Folium installed and imported!')


# In[4]:


# define the world map
world_map = folium.Map()

# display world map
world_map


# In[5]:


# Let's create a map centered around Canada and play with the zoom level to see how it affects the rendered map.

# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)

# display world map
world_map


# In[6]:


# Let's create the map again with a higher zoom level.

# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)

# display world map
world_map


# In[7]:


# The higher the zoom level the more the map is zoomed into the given center.


# In[8]:


# Question 1: Create a map of Mexico with a zoom level of 4.

    #define Mexico's geolocation coordinates
mexico_latitude = 23.6345 
mexico_longitude = -102.5528

    # define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)

    # display world map
mexico_map


# In[9]:


# Map Styles


# In[10]:


# Let's create a Stamen Toner map of canada with a zoom level of 4.

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')

# display map
world_map


# In[11]:


# Let's create a Stamen Terrain map of Canada with zoom level 4.

# create a Stamen Terrain map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Terrain')

# display map
world_map


# In[12]:


# Question 2: Create a map of Mexico to visualize its hill shading and natural vegetation. Use a zoom level of 6.

    #define Mexico's geolocation coordinates
mexico_latitude = 23.6345 
mexico_longitude = -102.5528

    # define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=6, tiles='Stamen Terrain')

    # display world map
mexico_map


# In[13]:


# Maps with Markers


# In[14]:


# Let's download and import the data on police department incidents using pandas `read_csv()` method.


# In[15]:


df_incidents = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe!')


# In[16]:


df_incidents.head()


# In[17]:


# So each row consists of 13 features:

# 1. IncidntNum: Incident Number
# 2. Category: Category of crime or incident
# 3. Descript: Description of the crime or incident
# 4. DayOfWeek: The day of week on which the incident occurred
# 5. Date: The Date on which the incident occurred
# 6. Time: The time of day on which the incident occurred
# 7. PdDistrict: The police department district
# 8. Resolution: The resolution of the crime in terms whether the perpetrator was arrested or not
# 9. Address: The closest address to where the incident took place
# 10. X: The longitude value of the crime location 
# 11. Y: The latitude value of the crime location
# 12. Location: A tuple of the latitude and the longitude values
# 13. PdId: The police department ID


# In[18]:


df_incidents.shape


# In[19]:


# The dataframe consists of 150,500 crimes, which took place in the year 2016. 

# In order to reduce computational cost, let's just work with the first 100 incidents in this dataset.


# In[20]:


# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]


# In[21]:


df_incidents.shape


# In[22]:


# Let's visualize where these crimes took place in the city of San Francisco. 

# We will use the default style, and we will initialize the zoom level to 12.


# In[23]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42


# In[24]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# In[25]:


# Now let's superimpose the locations of the crimes onto the map. 

# The way to do that in Folium is to create a feature group with its own features and style and then add it to the `sanfran_map`


# In[26]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
sanfran_map.add_child(incidents)


# In[27]:


# You can also add some pop-up text that would get displayed when you hover over a marker. 

# Let's make each marker display the category of the crime when hovered over.


# In[28]:


# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)


# In[29]:


# Now you are able to know what crime category occurred at each marker.


# In[30]:


# If you find the map to be so congested will all these markers, there are two remedies to this problem. 

# The simpler solution is to remove these location markers and just add the text to the circle markers themselves


# In[31]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.CircleMarker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)

# show map
sanfran_map


# In[32]:


# The other proper remedy is to group the markers into different clusters. 

# Each cluster is then represented by the number of crimes in each neighborhood. 

# These clusters can be thought of as pockets of San Francisco which you can then analyze separately.

# To implement this, we start off by instantiating a *MarkerCluster* object and adding all the data points in the dataframe 
  # to this object.


# In[33]:


from folium import plugins

# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
sanfran_map


# In[34]:


# When you zoom out all the way, all markers are grouped into one cluster, the global cluster, of 100 markers or crimes. 

# Once you start zooming in, the global cluster will start breaking up into smaller clusters. 

# Zooming in all the way will result in individual markers.


# In[35]:


# Choropleth Maps


# In[36]:


# let's create our own `Choropleth` map of the world depicting immigration from various countries to Canada.


# In[37]:


# Download the Canadian Immigration dataset and read it into a pandas dataframe.

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

print('Data downloaded and read into a dataframe!')


# In[38]:


df_can.head()


# In[39]:


# print the dimensions of the dataframe
print(df_can.shape)


# In[40]:


# In order to create a `Choropleth` map, we need a GeoJSON file that defines the areas/boundaries of the state, 
# county, or country that we are interested in. 

# In our case, since we are endeavoring to create a world map, we want a GeoJSON that defines the boundaries of all world 
# countries. 

# let's go ahead and download it. Let's name it world_countries.json.


# In[41]:


# download countries geojson file
get_ipython().system(' wget --quiet https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json')
    
print('GeoJSON file downloaded!')


# In[42]:


# let's create a world map, centered around **[0, 0]** *latitude* and *longitude* values, with an initisal zoom level of 2.

world_geo = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json' # geojson file

# create a plain world map
world_map = folium.Map(location=[0, 0], zoom_start=2)


# In[43]:


# Now to create a `Choropleth` map, we will use the choropleth method with the following main parameters:

    # 1. `geo_data`, which is the GeoJSON file.
    # 2. `data`, which is the dataframe containing the data.
    # 3. `columns`, which represents the columns in the dataframe that will be used to create the `Choropleth` map.
    # 4. `key_on`, which is the key or variable in the GeoJSON file that contains the name of the variable of interest. 
        # To determine that, you will need to open the GeoJSON file using any text editor and note the name of the key 
        # or variable that contains the name of the countries, since the countries are our variable of interest. 
        # In this case, name is the key in the GeoJSON file that contains the name of the countries. 
        # Note that this key is case_sensitive, so you need to pass exactly as it exists in the GeoJSON file.


# In[44]:


# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
world_map.choropleth(
    geo_data=world_geo,
    data=df_can,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Immigration to Canada'
)

# display map
world_map


# In[45]:


# Notice how the legend is displaying a negative boundary or threshold. 

# Let's fix that by defining our own thresholds and starting with 0 instead of -6,918!


# In[46]:


world_geo = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json' # geojson file

# create a numpy array of length 6 and has linear spacing from the minimum total immigration to the maximum total immigration
threshold_scale = np.linspace(df_can['Total'].min(),
                              df_can['Total'].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist() # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1 # make sure that the last value of the list is greater than the maximum immigration

# let Folium determine the scale.
world_map = folium.Map(location=[0, 0], zoom_start=2)
world_map.choropleth(
    geo_data=world_geo,
    data=df_can,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    threshold_scale=threshold_scale,
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Immigration to Canada',
    reset=True
)
world_map


# In[ ]:





# In[ ]:




