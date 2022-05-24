#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Importing packages 
import warnings; warnings.filterwarnings(action='ignore')
get_ipython().run_line_magic('matplotlib', 'inline')

#for Netcdf manipulation
import xarray as xr

#import rioxarray
from netCDF4 import Dataset
import netCDF4 as nc

#for array manipulation
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Grouper

#for plotting
import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap # plots maps
from matplotlib.cbook import dedent
import seaborn as sns
import cmocean


# In[2]:


#-----Read in volume dataset
f = '/Users/fridaperez/Developer/repos/volume-thickness/Volume_ENV-CYS_2002-2018_25000smth4.nc'
data = xr.open_dataset(f)


# In[3]:


volume = data.volume


# In[4]:


vol_time_mean = volume.mean(dim='time')


# In[5]:


# load lat-lon-value of the source data
fr = Dataset('/Users/fridaperez/Developer/repos/volume-thickness/Volume_ENV-CYS_2002-2018_25000smth3.nc') # loading this file because it gives us the longitude
vol = fr.variables['volume'][:]  #we are looking at the first timestep here 
lat = fr.variables['lat'][:]
lon = fr.variables['lon'][:]
#fr.close()


# In[13]:


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#plt.style.use("dark_background")


map = Basemap(projection='spstere',boundinglat=-50,lon_0=180,resolution='l')
fig = plt.figure(figsize=(12,12))
x, y = map(lon, lat)


map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='white',lake_color='white')
map.drawcoastlines()

# Draw parallels and Meridians
#map.drawparallels(np.arange(-80.,0.,20.),color='grey')
meridians = np.arange(-180.,181.,20.)
#map.drawmeridians(meridians,labels=[True,True,True,True],color='grey')
map.contourf(x,y,vol_time_mean,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])

# # KING HAKON VII
# lon_I = 30
# lat_I = -54
# x_I, y_I = map(lon_I, lat_I)
# plt.text(x_I, y_I, 'King Hakon VII', fontsize=18,fontweight='bold',color='white')
# # EAST ANTARCTICA
# lon_P = 144
# lat_P = -54
# x_P, y_P = map(lon_P, lat_P)
# plt.text(x_P, y_P, 'East Antarctica',fontsize=18,fontweight='bold',color='white')
# # ROSS AMUNDSEN SEA
# lon_R = -135
# lat_R = -50
# x_R, y_R = map(lon_R, lat_R)
# plt.text(x_R, y_R, 'Ross/\nAmundsen Sea',fontsize=18,fontweight='bold',color='white')
# # Amundsen-Bellingshausen
# lon_A = -94
# lat_A = -52
# x_A, y_A = map(lon_A, lat_A)
# plt.text(x_A, y_A, 'Amundsen\nBellingshausen\nSea',fontsize=18,fontweight='bold',color='white')
# # Weddell Sea 
# lon_W = -46
# lat_W = -50
# x_W, y_W = map(lon_W, lat_W)
# plt.text(x_W, y_W, 'Weddell \n Sea',fontsize=18,fontweight='bold',color='white')

# Colobar 
cbar = plt.colorbar(orientation='horizontal',shrink=0.7)
plt.tight_layout(pad=0.02, w_pad=0.01, h_pad=0.5)
cbar.ax.tick_params(labelsize=12) 
cbar.set_label(' Sea Ice Volume (km\u00b3)')
# Save Figure
#plt.style.use("dark_background")
plt.savefig('/Users/fridaperez/Desktop/VolRegionsmeanMap_light.png', dpi=300)


# In[7]:


# Yearly Means (volume)
# Weddell : 923.0075876771184
# East Antarctica : 516.3747253922787
# Ross/Amundsen :  1131.4146581435912
# Amundsen Bellingshausen : 881.6142083146052
# King Hakon VII : 838.7214187900964


# In[ ]:


# Yearly Means (Volume)
# Weddell : 923.0075876771184
# East Antarctica : 516.3747253922787
# Ross/Amundsen :  1131.4146581435912
# Amundsen Bellingshausen : 881.6142083146052
# King Hakon VII : 838.7214187900964

