#!/usr/bin/env python
# coding: utf-8

# In[]:
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
# import matplotlib.pylab as plt
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
time = data.time
time = pd.to_datetime(time.data) #turning dates into a data frame
df = data.volume

# In[5]:
# # Delineating Antarctic Regions
# ### Ross-Amundsen Advance/Retreat
## Create a matrix that is True where latitude is between 89S and 40S and False otherwise.
lat_bounds = np.logical_and(df.latitude  >= -89.83, df.latitude <= -39.36)
## Create a matrix that is True where longitude is between 70E and 165W and False otherwise.
lon_bounds = np.logical_and(df.longitude <=165.282, df.longitude <= -110.524)
lat_lon_bounds = np.logical_and(lat_bounds, lon_bounds)
## Finally, use where to mask out all volume values that do not fall within our lat_lon_bounds
subset_space = df.where(lat_lon_bounds, np.nan)

## Here we must change it to a float so that it can be handled by numpy
#EA_subset_space = EA_subset_space.to_array()
subset_space = subset_space.astype('float64')


# In[6]:
np.nanmean(subset_space)

# ### Year and Month averages

#----------------Advance/Retreat------------------#
year_idx = subset_space.groupby('time.year').groups
month_idx = subset_space.groupby('time.month').groups


# In[8]:
yr_mean = []
for year in year_idx:
    print(year)
    mean = np.nanmean(subset_space[subset_space.time.dt.year==year])
    yr_mean.append(mean)
# In[9]:
mon_mean = []
for mon in month_idx:
    print(mon)
    mean = np.nanmean(subset_space[subset_space.time.dt.month==mon])
    mon_mean.append(mean)

# In[10]:
# ### Let's assign the months to a pandas dataframe
Adv_Year = pd.DataFrame(yr_mean,dtype='float64')
Adv_Month = pd.DataFrame(mon_mean,dtype='float64')

# In[11]
#--------------Renaming the columns
Adv_Month = Adv_Month.rename({0: "Volume"}, axis='columns')


# In[12]:
#--------------Get dates into a dataframe
Dates = pd.DataFrame(time,dtype='datetime64')
Dates = Dates.rename({0: "Dates"}, axis='columns')

# In[13]:
##--------combining two dataframes---------##
frames =[Dates,Adv_Month]
table_month = pd.concat(frames,axis=1) #axis 1,refers to the join being in columns
table_month.info()  #making sure the Dates and Volume column are in the correct type
table_month['month'] = pd.DatetimeIndex(table_month['Dates']).month
table_month.info()

# In[17]:
import calendar
table_month['month'] = table_month['month'].apply(lambda x: calendar.month_abbr[x])
# In[19]:
# ### Let's assign the years to a pandas dataframe
#--------------Renaming the columns
Adv_Year = Adv_Year.rename({0: "Volume"}, axis='columns')
##--------combining two dataframes---------##
frames_yr =[Dates,Adv_Year]
table_yr = pd.concat(frames_yr,axis=1) #axis 1,refers to the join being in columns
table_yr.info()  #making sure the Dates and Volume column are in the correct type
table_yr['year'] = pd.DatetimeIndex(table_yr['Dates']).year
# In[25]:
# ## Next we will output the tables as csv's to combine with the other regions
table_month.to_csv('/Users/fridaperez/Developer/repos/local_repo/vol_regions_files/Ross_Am_02-18_months.csv')
table_yr.to_csv('/Users/fridaperez/Developer/repos/local_repo/vol_regions_files/Ross_Am_02-18_years.csv')


