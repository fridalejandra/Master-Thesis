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

# In[2]:
#-----Read in volume dataset
f = '/Users/fridaperez/Developer/repos/local_repo/Volume_SH_ENV-CY2_2002-2018.nc'
data = xr.open_dataset(f)

# In[4]:
time = data.time
time = pd.to_datetime(time.data) #turning dates into a data frame

# In[5]:
df = data.volume

# In[6]:
# # Delineating Antarctic Regions

# ### KHVII Advance
## Create a matrix that is True where latitude is between 89S and 40S and False otherwise.
lat_bounds = np.logical_and(df.latitude  >= -89.83, df.latitude <= -39.36)
## Create a matrix that is True where longitude is between 70E and 165W and False otherwise.
lon_bounds = np.logical_and(df.longitude >= -25, df.longitude <= 70)
lat_lon_bounds = np.logical_and(lat_bounds, lon_bounds)
## Finally, use where to mask out all volume values that do not fall within our lat_lon_bounds
subset_space = df.where(lat_lon_bounds, np.nan)

## Here we must change it to a float so that it can be handled by numpy
subset_space = subset_space.astype('float64')

# In[7]:
np.nanmean(subset_space)
# In[8]:
# ### KVHII Retreat
## Create a matrix that is True where latitude is between 89S and 40S and False otherwise.
lat_boundsR = np.logical_and(df.latitude  >= -89.83, df.latitude <= -39.36)
## Create a matrix that is True where longitude is between 70E and 165W and False otherwise.
lon_boundsR = np.logical_and(df.longitude >= -15, df.longitude <= 70)
lat_lon_boundsR = np.logical_and(lat_boundsR, lon_boundsR)
## Finally, use where to mask out all volume values that do not fall within our lat_lon_bounds
subset_spaceR = df.where(lat_lon_boundsR, np.nan)

## Here we must change it to a float so that it can be handled by numpy
#subset_spaceR = subset_spaceR.to_array()
subset_spaceR = subset_spaceR.astype('float64')
# In[9]:
# ### Year and Month averages
#----------------Advance------------------#
year_idx = subset_space.groupby('time.year').groups
month_idx = subset_space.groupby('time.month').groups
#----------------Retreat------------------#
year_idxs = subset_spaceR.groupby('time.year').groups
month_idxs = subset_spaceR.groupby('time.month').groups

# In[10]:
yr_mean = []
for year in year_idx:
    print(year)
    mean = np.nanmean(subset_space[subset_space.time.dt.year==year])
    yr_mean.append(mean)

# In[11]:
mon_mean = []
for mon in month_idx:
    print(mon)
    mean = np.nanmean(subset_space[subset_space.time.dt.month==mon])
    mon_mean.append(mean)
# In[12]:
yr_meanR = []
for year in year_idxs:
    print(year)
    mean = np.nanmean(subset_spaceR[subset_spaceR.time.dt.year==year])
    yr_meanR.append(mean)

# In[13]:
mon_meanR = []
for mon in month_idxs:
    print(mon)
    mean = np.nanmean(subset_spaceR[subset_spaceR.time.dt.month==mon])
    mon_meanR.append(mean)

# In[14]:
Adv_Year = pd.DataFrame(yr_mean)
Adv_Month = pd.DataFrame(mon_mean)
Re_Year = pd.DataFrame(yr_meanR)
Re_Month = pd.DataFrame(mon_meanR)
# In[15]:
# ### Let's assign the months to a pandas dataframe
Adv_Year = pd.DataFrame(yr_mean,dtype='float64')
Adv_Month = pd.DataFrame(mon_mean,dtype='float64')

# In[16]:
#--------------Renaming the columns
Adv_Month = Adv_Month.rename({0: "Volume"}, axis='columns')

# In[17]:
#--------------Get dates into a dataframe
Dates = pd.DataFrame(time,dtype='datetime64')
Dates = Dates.rename({0: "Dates"}, axis='columns')

# In[18]:
##--------combining two dataframes---------##
frames =[Dates,Adv_Month]
table_month = pd.concat(frames, axis=1) #axis 1,refers to the join being in columns
table_month.info()  #making sure the Dates and Volume column are in the correct type
table_month['month'] = pd.DatetimeIndex(table_month['Dates']).month
import calendar
table_month['month'] = table_month['month'].apply(lambda x: calendar.month_abbr[x])
# In[22]:
# ### Let's assign the years to a pandas dataframe
#--------------Renaming the columns
Adv_Year = Adv_Year.rename({0: "Volume"}, axis='columns')
##--------combining two dataframes---------##
frames_yr =[Dates,Adv_Year]
table_yr = pd.concat(frames_yr,axis=1) #axis 1,refers to the join being in columns
table_yr['year'] = pd.DatetimeIndex(table_yr['Dates']).year
# In[25]:
# ## Next we will output the tables as csv's to combine with the other regions
table_month.to_csv('/Users/fridaperez/Developer/repos/local_repo/vol_regions_files/KVHII_02-18_months.csv')
table_yr.to_csv('/Users/fridaperez/Developer/repos/local_repo/vol_regions_files/KVHII_02-18_years.csv')




