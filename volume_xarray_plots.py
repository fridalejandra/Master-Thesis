#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings; warnings.filterwarnings(action='ignore')
get_ipython().run_line_magic('matplotlib', 'inline')
#for Netcdf manipulation
import xarray as xr
from netCDF4 import Dataset
import netCDF4 as nc

#for array manipulation
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Grouper

#for plotting
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap # plots maps
from matplotlib.cbook import dedent

import cmocean


# In[2]:
# Read in volume files
#volume_file = '/Users/fridaperez/Developer/repos/local_repo/Volume_SH_ENV-CY2_2002-2018.nc'
volume_file = '/Users/fridaperez/Developer/repos/local_repo/VolInv_SH_ENV-CY2_2002-2018.nc' # invertlat

data = xr.open_dataset(volume_file)

##Read in SIT file to add coordinates
sit_file = '/Users/fridaperez/Developer/repos/local_repo/SIT_25000/SIT_SH_Filled-316x332.nc'
data_sit = xr.open_dataset(sit_file)
lon_t = data_sit.longitude
lat_t = data_sit.latitude
sit = data_sit.SIT
# In[5]:
siv = data.volume

# In[7]:
#Fixing the dates for SIT data set for 2002-2011
time = data.time #getting time var from xarray
dates_vol = pd.to_datetime(time.data) #turning dates into a data frame
print(dates_vol)
# In[8]:
time= pd.DataFrame(dates_vol)
# In[9]:
vol_mean=[]
for y in range(len(data.volume)):
    mean = np.nanmean(data.volume[y])
    vol_mean.append(mean)
# In[10]:
print(vol_mean)
# In[11]:
df_vol = pd.DataFrame(vol_mean)
# In[12]:
df_vol=df_vol.rename({0: "SIV"}, axis='columns')
time = time.rename({0: "Dates"}, axis='columns')
# In[13]:
frames =[time,df_vol]
table = pd.concat(frames,axis=1)
# In[14]:
print(table)
# In[15]:
# round to two decimal places in python pandas
pd.options.display.float_format = '{:.2f}'.format
table.info()
import matplotlib.pyplot as plt # Impot the relevant module

fig, ax = plt.subplots() # Create the figure and axes object
# Plot the first x and y axes:
ax=table.plot(x = 'Dates', y = 'SIV', ax = ax, label='Sea Ice Volume', color="steelblue")
ax.set_ylabel('SIV (km$a^{3}$)')
ax.set_title('Annual Sea Ice Volume 2002-2018')
ax.get_legend().remove()
#plt.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/annualcycle_vol.pdf')
# In[17]:

# ## Yearly
yearly_means = data.groupby("time.year").mean()
# xarray's groupby reductions drop attributes. Let's assign them back so we get nice labels.
yearly_means.volume.attrs = data.volume.attrs


# In[19]:

fg = yearly_means.volume.plot(col="year", col_wrap=6,cmap=cmocean.cm.ice, vmin=0, vmax=3000)
titless = ["2002", "2003", "2004", "2005", "2006", "2007","2008","2009","2010","2011","2012","2013","2014",
           "2015","2016","2017","2018"]
for ax, title in zip(fg.axes.flat, titless):
    ax.set_title(title)
#fg.fig.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/white_ExtendedVol_yearlyHorizontal.png')


# In[20]:

monthly_means = data.groupby("time.month").mean()
# xarray's groupby reductions drop attributes. Let's assign them back so we get nice labels.
monthly_means.volume.attrs = data.volume.attrs
monthly_means


# In[21]:

f = monthly_means.volume.plot(col="month", col_wrap=3,cmap=cmocean.cm.ice, vmin=0, vmax=3000)
titles = ["May", "June", "July", "August", "September", "October"]
for ax, title in zip(f.axes.flat, titles):
    ax.set_title(title)
#f.fig.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/white_ExtendedVol_monthly.png')
#levels=[0,500,1000,1500,2000,2500,3000,3200]

# In[22]

monthly_means_sit = data_sit.groupby("time.month").mean()
monthly_means_sit.SIT

# In[23]
import calendar
table['month'] = table.Dates.dt.month
table['year'] = table.Dates.dt.year
table['month'] = table['month'].apply(lambda x:calendar.month_abbr[x])
# In[24]

import seaborn as sns
sns.relplot(data=table, x="year", y="SIV", hue="month", kind="line")
plt.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/SIV_month_linegraph.png', dpi=300)

# In[]
sns.relplot(data=table, x="month", y="SIV", hue="year", kind="line", palette="Paired")
plt.savefig('/Users/fridaperez/Developer/repos/local_repo/pub_plots/SIV_year_linegraph.png',dpi=300)

#%%
