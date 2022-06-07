#!/usr/bin/env python
# coding: utf-8

# In[1]:
#--------Import packages
import warnings; warnings.filterwarnings(action='ignore')
get_ipython().run_line_magic('matplotlib', 'inline')

#--------For Netcdf manipulation
import xarray as xr
from netCDF4 import Dataset
import netCDF4 as nc

#--------For array manipulation
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Grouper

#--------For plotting
# import cartopy.crs as ccrs
# import cartopy.feature as cfeature
import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap # plots maps
from matplotlib.cbook import dedent
import cmocean
import seaborn as sns
get_ipython().run_line_magic('config', 'Completer.use_jedi = False')


# In[2]:


#-----Read in volume dataset
f = '/Users/fridaperez/Developer/repos/local_repo/Volume_SH_ENV-CY2_2002-2018.nc'
data = xr.open_dataset(f)


# In[3]:
data_nc =  nc.Dataset(f)
lat = data_nc['latitude'][:]
lon = data_nc['longitude'][:]


# In[4]:
time = data.time
time = pd.to_datetime(time.data) #turning dates into a data frame

# In[5]:
df = data.volume

# In[6]:


siv_time_mean = df.mean(dim='time')

# In[7]:
# # Delineating Antarctic Regions

# ### Weddell Advance
## Create a matrix that is True where latitude is between 89S and 40S and False otherwise.
lat_bounds = np.logical_and(df.latitude  >= -89.83, df.latitude <= -39.36)
## Create a matrix that is True where longitude is between 70E and 165W and False otherwise.
lon_bounds = np.logical_and(df.longitude <= -25.1077, df.longitude >= -65.0715)## Combine the lat_bounds and lon_bounds logical matrices:
    
lat_lon_bounds = np.logical_and(lat_bounds, lon_bounds)
## Finally, use where to mask out all volume values that do not fall within our lat_lon_bounds
subset_space = df.where(lat_lon_bounds, np.nan)

## Here we must change it to a float so that it can be handled by numpy
subset_space = subset_space.astype('float64')


# In[8]:
np.nanmean(subset_space)
# In[9]:
#
# m = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = m(lon,lat)
# fig = plt.figure(figsize=(12,12))
# m.fillcontinents(color='white',lake_color='white')
# m.drawcoastlines()
# m.drawparallels(np.arange(-80.,0.,20.))
# m.drawmeridians(np.arange(-180.,181.,20.))
# m.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# m.contourf(x,y,subset_space.isel(time=50),40,cmap=cmap0)
# #transform=ccrs.SouthPolarStereo()
# plt.colorbar(label=u'Sea ice volume')


# In[44]:
# map = Basemap(projection='spstere',boundinglat=-50,lon_0=180,resolution='l')
# fig = plt.figure(figsize=(12,12))
# x, y = map(lon, lat)
#
#
# map.drawmapboundary(fill_color='lightblue')
# map.fillcontinents(color='white',lake_color='grey')
# map.drawcoastlines()
#
# # Draw parallels and Meridians
# map.drawparallels(np.arange(-80.,0.,20.),color='white')
# meridians = np.arange(-180.,181.,20.)
# map.drawmeridians(meridians,labels=[True,True,True,True],color='white')
# #cmap0 = plt.cm.get_cmap(cmocean.cm.ice, 11)
# map.contourf(x,y,siv_time_mean,40,cmap= cmocean.cm.ice, levels= [1,500,1000,1500,2000,2500,3000, 3200])
#
# # KING HAKON VII
# lon_I = 30
# lat_I = -54
# x_I, y_I = map(lon_I, lat_I)
# plt.text(x_I, y_I, 'King Hakon\nVII', fontsize=18,fontweight='bold',color='black')
# # EAST ANTARCTICA
# lon_P = 150
# lat_P = -52
# x_P, y_P = map(lon_P, lat_P)
# plt.text(x_P, y_P, 'East\nAntarctica',fontsize=18,fontweight='bold',color='black')
# # ROSS AMUNDSEN SEA
# lon_R = -137
# lat_R = -45
# x_R, y_R = map(lon_R, lat_R)
# plt.text(x_R, y_R, 'Ross-\nAmundsen Sea',fontsize=18,fontweight='bold',color='black')
# # Amundsen-Bellingshausen
# lon_A = -94
# lat_A = -52
# x_A, y_A = map(lon_A, lat_A)
# plt.text(x_A, y_A, 'ABS',fontsize=18,fontweight='bold',color='black')
# # Weddell Sea
# lon_W = -46
# lat_W = -45
# x_W, y_W = map(lon_W, lat_W)
# plt.text(x_W, y_W, 'Weddell \nSea',fontsize=18,fontweight='bold',color='black')
# #transform=ccrs.SouthPolarStereo()
# plt.colorbar(label=u'Sea ice volume (km3)', orientation = 'horizontal')
# plt.savefig('/Users/fridaperez/Desktop/volumeexport.png', dpi=300)
#

# In[ ]:
# ### Weddell Retreat

## Create a matrix that is True where latitude is between 89S and 40S and False otherwise.
lat_boundsR = np.logical_and(df.latitude >= -89.83, df.latitude <= -39.36)
## Create a matrix that is True where longitude is between 70E and 165W and False otherwise.
lon_boundsR = np.logical_and(df.longitude <= -15.0, df.longitude >= -70.0)

lat_lon_boundsR = np.logical_and(lat_boundsR, lon_boundsR)
## Finally, use where to mask out all volume values that do not fall within our lat_lon_bounds
subset_spaceR = df.where(lat_lon_boundsR, np.nan)

## Here we must change it to a float so that it can be handled by numpy
#subset_spaceR = subset_spaceR.to_array()
subset_spaceR = subset_spaceR.astype('float64')

# In[ ]:
# ### Year and Month averages
#----------------Advance------------------#
year_idx = subset_space.groupby('time.year').groups
month_idx = subset_space.groupby('time.month').groups
#----------------Retreat------------------#
year_idxs = subset_spaceR.groupby('time.year').groups
month_idxs = subset_spaceR.groupby('time.month').groups


# In[ ]:
yr_mean = []
for year in year_idx:
    print(year)
    mean = np.nanmean(subset_space[subset_space.time.dt.year==year])
    yr_mean.append(mean)

# In[ ]:
mon_mean = []
for mon in month_idx:
    print(mon)
    mean = np.nanmean(subset_space[subset_space.time.dt.month==mon])
    mon_mean.append(mean)

# In[ ]:
yr_meanR = []
for year in year_idxs:
    print(year)
    mean = np.nanmean(subset_spaceR[subset_spaceR.time.dt.year==year])
    yr_meanR.append(mean)

# In[ ]:
mon_meanR = []
for mon in month_idxs:
    print(mon)
    mean = np.nanmean(subset_spaceR[subset_spaceR.time.dt.month==mon])
    mon_meanR.append(mean)

# In[ ]:
Adv_Year = pd.DataFrame(yr_mean)
Adv_Month = pd.DataFrame(mon_mean)

Re_Year = pd.DataFrame(yr_meanR)
Re_Month = pd.DataFrame(mon_meanR)

# In[ ]:
# ### Let's assign the months to a pandas dataframe

Adv_Year = pd.DataFrame(yr_mean,dtype='float64')
Adv_Month = pd.DataFrame(mon_mean,dtype='float64')

#--------------Renaming the columns
Adv_Month = Adv_Month.rename({0: "Volume"}, axis='columns')

#--------------Get dates into a dataframe
Dates = pd.DataFrame(time,dtype='datetime64')
Dates = Dates.rename({0: "Dates"}, axis='columns')

##--------combining two dataframes---------##
frames =[Dates,Adv_Month]
table_month = pd.concat(frames,axis=1) #axis 1,refers to the join being in columns
table_month.info()  #making sure the Dates and Volume column are in the correct type
table_month['month'] = pd.DatetimeIndex(table_month['Dates']).month
# In[ ]:
import calendar
table_month['month'] = table_month['month'].apply(lambda x: calendar.month_abbr[x])


# ### Let's assign the years to a pandas dataframe
#--------------Renaming the columns
Adv_Year = Adv_Year.rename({0: "Volume"}, axis='columns')
##--------combining two dataframes---------##
frames_yr =[Dates,Adv_Year]
table_yr = pd.concat(frames_yr,axis=1) #axis 1,refers to the join being in columns


# In[ ]:
table_yr['year'] = pd.DatetimeIndex(table_yr['Dates']).year
# ## Next we will output the tables as csv's to combine with the other regions
table_month.to_csv('/Users/fridaperez/Developer/repos/local_repo/vol_regions_files/Weddell_02-18_months.csv')
table_yr.to_csv('/Users/fridaperez/Developer/repos/local_repo/vol_regions_files/Weddell_02-18_years.csv')

# In[ ]:




