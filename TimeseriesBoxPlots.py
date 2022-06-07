#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for Netcdf manipulation
import xarray as xr
from netCDF4 import Dataset
import netCDF4 as nc

#for array manipulation
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Grouper
import matplotlib.pyplot as plt #plotting package
import seaborn as sns; sns.set(color_codes=True) # plotting aes
plt.style.use('ggplot')


# In[2]:


##Read in SIT file to add coordinates
sit_file = '/Users/fridaperez/Developer/repos/local_repo/SIT_25000/SIT_SH_Filled-316x332.nc'
data_sit = xr.open_dataset(sit_file)
lon_t = data_sit.longitude
lat_t = data_sit.latitude


# In[3]:


# Read in volume files 
volume_files = '/Users/fridaperez/Developer/repos/local_repo/Volume_SH_ENV-CY2_2002-2018.nc'
data = xr.open_dataset(volume_files)

# In[5]:
volume = data.volume
sit = data_sit.SIT

# In[6]:

time = data.time #getting time var from xarray
dates_vol = pd.to_datetime(time.data) #turning dates into a data frame
print(dates_vol) 


# In[7]:


time = pd.DataFrame(dates_vol)


# In[8]:
sit_mean = []
for y in range(len(sit)):
    mean = np.nanmean(sit[y])
    sit_mean.append(mean)


# In[9]:
vol_mean=[]
for y in range(len(data.volume)):
    mean = np.nanmean(data.volume[y])
    vol_mean.append(mean)

# In[10]:
df_vol = pd.DataFrame(vol_mean)
df_sit = pd.DataFrame(sit_mean)

# In[11]:
df_vol = df_vol.rename({0: "Volume"}, axis='columns')
df_sit = df_sit.rename({0: "SIT"}, axis='columns')
time = time.rename({0: "Dates"}, axis='columns')

# In[12]:
frames =[time,df_vol,df_sit]
table = pd.concat(frames,axis=1)
table = table.set_index(table['Dates'])

# In[13]:
#fig, ax = plt.subplots()
#plt.style.use("dark_background")
ax = table.assign(year=table.index.year).boxplot(column='Volume', by='year', figsize=(12, 6))
ax.set_ylabel('Volume (km\u00b3)')
plt.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/Volbox_year_light.png', dpi=300)


# In[14]:
#fig, ax = plt.subplots()
#plt.style.use("dark_background")
ax = table.assign(year=table.index.year).boxplot(column='SIT', by='year', figsize=(12, 6))
ax.set_ylabel('SIT (m)')
plt.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/SITbox_year_light.png', dpi=300)


# In[15]:
#fig, ax = plt.subplots()
#plt.style.use("dark_background")
ax = table.assign(month=table.index.month).boxplot(column='Volume', by='month', figsize=(12, 6))
ax.set_ylabel('Volume (km\u00b3)')
#plt.savefig('/Users/fridaperez/Desktop/Volbox_month_dark.png', dpi=300)

# In[16]:
#fig, ax = plt.subplots()
#plt.style.use("dark_background")
ax = table.assign(month=table.index.month).boxplot(column='SIT', by='month', figsize=(12, 6))
ax.set_ylabel('SIT (m)')
#plt.savefig('/Users/fridaperez/Desktop/SITbox_month_dark.png', dpi=300)

# In[ ]:




