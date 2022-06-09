#!/usr/bin/env python
# coding: utf-8

# In[1]:
# ## Import Libraries

#import warnings; warnings.filterwarnings(action='ignore')
#get_ipython().run_line_magic('matplotlib', 'inline')
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
# #import cartopy.feature as cfeature
# import matplotlib.pylab as plt
# from mpl_toolkits.basemap import Basemap # plots maps
# from matplotlib.cbook import dedent

import cmocean

# In[2]:
#Reading files with xarray 
siv_file = '/Users/fridaperez/Developer/repos/local_repo/VolInv_SH_ENV-CY2_2002-2018.nc'  # prepping path for xr
data_siv = xr.open_dataset(siv_file) # opening sit for xarray


# In[3]:

# Here we want to read the SIV files using the nc package
siv_nc = nc.Dataset("/Users/fridaperez/Developer/repos/local_repo/Volume_SH_ENV-CY2_2002-2018.nc") #reading SIV from nc
#reading in SIV variables 02-11
time = siv_nc.variables['time'][:]  #sit time
lat=siv_nc.variables['latitude'][:]
lon=siv_nc.variables['longitude'][:]
siv=siv_nc.variables['volume'][:,:,:]
# siv_y=siv_nc.variables['ygrid'][:]
# siv_x=siv_nc.variables['xgrid'][:]

#newset=datos.rename_vars({'__xarray_dataarray_variable__':'volume'})

# ##Year Volume
# year_idx = data.groupby('time.year').groups
# year_03 = year_idx[2003]
# year_04 = year_idx[2004]
# year_05 = year_idx[2005]
# year_06 = year_idx[2006]
# year_07 = year_idx[2007]
# year_08 = year_idx[2008]
# year_09 = year_idx[2009]
# year_10 = year_idx[2010]
# year_11 = year_idx[2011]


# In[17]:
# # VOLUME #
# # Extract years by selecting 
# # the relevant indices
# gs_03=data.isel(time=year_03)
# gs_04=data.isel(time=year_04)
# gs_05=data.isel(time=year_05)
# gs_06=data.isel(time=year_06)
# gs_07=data.isel(time=year_07)
# gs_08=data.isel(time=year_08)
# gs_09=data.isel(time=year_09)
# gs_10=data.isel(time=year_10)
# gs_11=data.isel(time=year_11)


# In[18]:
# the relevant indices
yeardata = data_siv.volume.groupby('time.year').mean('time',keep_attrs=True)
gs_03=yeardata.sel(year=2003)
gs_04=yeardata.sel(year=2004)
gs_05=yeardata.sel(year=2005)
gs_06=yeardata.sel(year=2006)
gs_07=yeardata.sel(year=2007)
gs_08=yeardata.sel(year=2008)
gs_09=yeardata.sel(year=2009)
gs_10=yeardata.sel(year=2010)
gs_11=yeardata.sel(year=2011)
gs_12=yeardata.sel(year=2012)
gs_13=yeardata.sel(year=2013)
gs_14=yeardata.sel(year=2014)
gs_15=yeardata.sel(year=2015)
gs_16=yeardata.sel(year=2016)
gs_17=yeardata.sel(year=2017)
gs_18=yeardata.sel(year=2018)
# In[35]:
#import matplotlib
#matplotlib.use('PS')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap # plots maps
import cmocean
#plt.style.use('dark_background')
### YEAR ###
fig = plt.figure(figsize=[12,10])
#2003
ax = fig.add_subplot(451)
ax.set_title("2003")
m = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = m(lon, lat)
m.fillcontinents(color='white',lake_color='white')
m.drawcoastlines()
m.drawparallels(np.arange(-80.,0.,20.))
m.drawmeridians(np.arange(-180.,181.,20.))
m.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
clr2=m.contourf(x,y,gs_03,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2004
ax = fig.add_subplot(452)
ax.set_title("2004")

j = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = j(lon, lat)
j.fillcontinents(color='white',lake_color='white')
j.drawcoastlines()
j.drawparallels(np.arange(-80.,0.,20.))
j.drawmeridians(np.arange(-180.,181.,20.))
j.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
j.contourf(x,y,gs_04,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2005
ax = fig.add_subplot(453)
ax.set_title("2005")
jj = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = jj(lon, lat)
jj.fillcontinents(color='white',lake_color='white')
jj.drawcoastlines()
jj.drawparallels(np.arange(-80.,0.,20.))
jj.drawmeridians(np.arange(-180.,181.,20.))
jj.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
jj.contourf(x,y,gs_05,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2006
ax = fig.add_subplot(454)
ax.set_title("2006")
a = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = a(lon, lat)
a.fillcontinents(color='white',lake_color='white')
a.drawcoastlines()
a.drawparallels(np.arange(-80.,0.,20.))
a.drawmeridians(np.arange(-180.,181.,20.))
a.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
a.contourf(x,y,gs_06,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#t#ransform=ccrs.SouthPolarStereo()

#2007
ax = fig.add_subplot(455)
ax.set_title("2007")
s = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = s(lon, lat)
s.fillcontinents(color='white',lake_color='white')
s.drawcoastlines()
s.drawparallels(np.arange(-80.,0.,20.))
s.drawmeridians(np.arange(-180.,181.,20.))
s.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
s.contourf(x,y,gs_07,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2008
ax = fig.add_subplot(456)
ax.set_title("2008")
oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = oc(lon, lat)
oc.fillcontinents(color='white',lake_color='white')
oc.drawcoastlines()
oc.drawparallels(np.arange(-80.,0.,20.))
oc.drawmeridians(np.arange(-180.,181.,20.))
oc.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
oc.contourf(x,y,gs_08,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2009
ax = fig.add_subplot(457)
ax.set_title("2009")
oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = oc(lon, lat)
oc.fillcontinents(color='white',lake_color='white')
oc.drawcoastlines()
oc.drawparallels(np.arange(-80.,0.,20.))
oc.drawmeridians(np.arange(-180.,181.,20.))
oc.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
oc.contourf(x,y,gs_09,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2010
ax = fig.add_subplot(458)
ax.set_title("2010")
oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = oc(lon, lat)
oc.fillcontinents(color='white',lake_color='white')
oc.drawcoastlines()
oc.drawparallels(np.arange(-80.,0.,20.))
oc.drawmeridians(np.arange(-180.,181.,20.))
oc.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
oc.contourf(x,y,gs_10,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2011
ax = fig.add_subplot(459)
ax.set_title("2011")
oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = oc(lon, lat)
oc.fillcontinents(color='white',lake_color='white')
oc.drawcoastlines()
oc.drawparallels(np.arange(-80.,0.,20.))
oc.drawmeridians(np.arange(-180.,181.,20.))
oc.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
oc.contourf(x,y,gs_12,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
#transform=ccrs.SouthPolarStereo()

#2012
ax = fig.add_subplot(4510)
ax.set_title("2012")
oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
x, y = oc(lon, lat)
oc.fillcontinents(color='white',lake_color='white')
oc.drawcoastlines()
oc.drawparallels(np.arange(-80.,0.,20.))
oc.drawmeridians(np.arange(-180.,181.,20.))
oc.drawmapboundary(fill_color='black')
cmap0 = plt.cm.get_cmap('jet', 11)
oc.contourf(x,y,gs_11,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])




#fig.suptitle(u'Sea ice volume 2003-2011', fontsize=15, y=1.1)
plt.subplots_adjust(wspace=0.05, hspace=0.05, right=0.8)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=0.5)
#cbar_ax = fig.add_axes([-0.05, 0.15, 0.02, 0.7])
cbar_axx = fig.add_axes([1, 0.15, 0.02, 0.7])
cbar_axx.tick_params(labelsize=18) 


fig.colorbar(clr2,cax=cbar_axx,label= u'\n Sea ice volume (km3)')
#fig.colorbar(clr1, cax=cbar_axx,label= 'SIT (m) mean')

# saving figure #
#plt.savefig('/Users/fridaperez/Desktop/year_volume_dark.png', dpi=300, bbox_inches='tight')

# showing figure # 
plt.show()


# ## Monthly

# In[ ]:


# # Use .groupby('time.month') to organize the data into months
# # then use .groups to extract the indices for each month
# month_idxs=data.groupby('time.month').groups

# # Extract the time indices corresponding to all the months 
# may_idxs=month_idxs[5]
# jun_idxs=month_idxs[6]
# jul_idxs=month_idxs[7]
# aug_idxs=month_idxs[8]
# sep_idxs=month_idxs[9]
# octo_idxs=month_idxs[10]


# In[ ]:


# # Extract the january months by selecting 
# # the relevant indices
# gs_may=data.isel(time=may_idxs)
# gs_jun=data.isel(time=jun_idxs)
# gs_jul=data.isel(time=jul_idxs)
# gs_aug=data.isel(time=aug_idxs)
# gs_sep=data.isel(time=sep_idxs)
# gs_octo=data.isel(time=octo_idxs)


# In[27]:


# Extract the january months by selecting 
# the relevant indices
mothsdatas = data_siv.volume.groupby('time.month').mean('time',keep_attrs=True)
gs_mays=mothsdatas.sel(month=5)
gs_juns=mothsdatas.sel(month=6)
gs_juls=mothsdatas.sel(month=7)
gs_augs=mothsdatas.sel(month=8)
gs_seps=mothsdatas.sel(month=9)
gs_octos=mothsdatas.sel(month=10)


# # In[28]:
#
#
# # Extract the january months by selecting
# # the relevant indices
# mothsdata = data.volume.groupby('time.month').mean('time',keep_attrs=True)
# gs_may=mothsdata.sel(month=5)
# gs_jun=mothsdata.sel(month=6)
# gs_jul=mothsdata.sel(month=7)
# gs_aug=mothsdata.sel(month=8)
# gs_sep=mothsdata.sel(month=9)
# gs_octo=mothsdata.sel(month=10)


# In[34]:

#
# #import matplotlib
# #matplotlib.use('PS')
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap # plots maps
# plt.style.use('dark_background')
# fig = plt.figure(figsize=[12,10])
#
# #May
# ax = fig.add_subplot(231)
# ax.set_title("May")
# m = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = m(lon, lat)
# m.fillcontinents(color='white',lake_color='white')
# m.drawcoastlines()
# m.drawparallels(np.arange(-80.,0.,20.))
# m.drawmeridians(np.arange(-180.,181.,20.))
# m.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# clr2=m.contourf(x,y,gs_may,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
# #transform=ccrs.SouthPolarStereo()
#
# #June
# ax = fig.add_subplot(232)
# ax.set_title("June")
#
# j = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = j(lon, lat)
# j.fillcontinents(color='white',lake_color='white')
# j.drawcoastlines()
# j.drawparallels(np.arange(-80.,0.,20.))
# j.drawmeridians(np.arange(-180.,181.,20.))
# j.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# j.contourf(x,y,gs_jun,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
# #transform=ccrs.SouthPolarStereo()
#
# #July
# ax = fig.add_subplot(233)
# ax.set_title("July")
# jj = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = jj(lon, lat)
# jj.fillcontinents(color='white',lake_color='white')
# jj.drawcoastlines()
# jj.drawparallels(np.arange(-80.,0.,20.))
# jj.drawmeridians(np.arange(-180.,181.,20.))
# jj.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# jj.contourf(x,y,gs_jul,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
# #transform=ccrs.SouthPolarStereo()
#
# #August
# ax = fig.add_subplot(234)
# ax.set_title("August")
# a = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = a(lon, lat)
# a.fillcontinents(color='white',lake_color='white')
# a.drawcoastlines()
# a.drawparallels(np.arange(-80.,0.,20.))
# a.drawmeridians(np.arange(-180.,181.,20.))
# a.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# a.contourf(x,y,gs_aug,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
# #transform=ccrs.SouthPolarStereo()
#
# #September
# ax = fig.add_subplot(235)
# ax.set_title("September")
# s = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = s(lon, lat)
# s.fillcontinents(color='white',lake_color='white')
# s.drawcoastlines()
# s.drawparallels(np.arange(-80.,0.,20.))
# s.drawmeridians(np.arange(-180.,181.,20.))
# s.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# s.contourf(x,y,gs_sep,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
# #transform=ccrs.SouthPolarStereo()
#
# #October
# ax = fig.add_subplot(236)
# ax.set_title("October")
# oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = oc(lon, lat)
# oc.fillcontinents(color='white',lake_color='white')
# oc.drawcoastlines()
# oc.drawparallels(np.arange(-80.,0.,20.))
# oc.drawmeridians(np.arange(-180.,181.,20.))
# oc.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# oc.contourf(x,y,gs_octo,40,cmap= cmocean.cm.ice,levels=[0,500,1000,1500,2000,2500,3000,3200])
# #transform=ccrs.SouthPolarStereo()
#
# #fig.suptitle(u'Monthly sea ice volume \n  2003-2011', fontsize=15, y=1)
# plt.subplots_adjust(wspace=0.05, hspace=0.05, right=0.8)
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# #cbar_ax = fig.add_axes([-0.05, 0.15, 0.02, 0.7])
# cbar_axx = fig.add_axes([1, 0.15, 0.02, 0.7])
# cbar_axx.tick_params(labelsize=18)
#
#
# fig.colorbar(clr2,cax=cbar_axx,label= u'\n Sea ice volume (km3)')
# #fig.colorbar(clr1, cax=cbar_axx,label= 'SIT (m) mean')
#
# # saving figure #
# #plt.savefig('/Users/fridaperez/Desktop/months_volume_dark.png', dpi=300, bbox_inches='tight')
#
# # showing figure #
# plt.show()
#
#
# # In[ ]:
#
#
# #import matplotlib
# #matplotlib.use('PS')
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap # plots maps
#
# fig = plt.figure(figsize=[12,10])
#
# #May
# ax = fig.add_subplot(231)
# ax.set_title("May")
# m = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = m(lon, lat)
# m.fillcontinents(color='white',lake_color='white')
# m.drawcoastlines()
# m.drawparallels(np.arange(-80.,0.,20.))
# m.drawmeridians(np.arange(-180.,181.,20.))
# m.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# clr2=m.contourf(x,y,gs_mays,40,cmap=cmap0,levels=[0,1,2,3,4,5])
# transform=ccrs.SouthPolarStereo()
#
# #June
# ax = fig.add_subplot(232)
# ax.set_title("June")
#
# j = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = j(lon, lat)
# j.fillcontinents(color='white',lake_color='white')
# j.drawcoastlines()
# j.drawparallels(np.arange(-80.,0.,20.))
# j.drawmeridians(np.arange(-180.,181.,20.))
# j.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# j.contourf(x,y,gs_juns,40,cmap=cmap0,levels=[0,1,2,3,4,5])
# transform=ccrs.SouthPolarStereo()
#
# #July
# ax = fig.add_subplot(233)
# ax.set_title("July")
# jj = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = jj(lon, lat)
# jj.fillcontinents(color='white',lake_color='white')
# jj.drawcoastlines()
# jj.drawparallels(np.arange(-80.,0.,20.))
# jj.drawmeridians(np.arange(-180.,181.,20.))
# jj.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# jj.contourf(x,y,gs_juls,40,cmap=cmap0,levels=[0,1,2,3,4,5])
# transform=ccrs.SouthPolarStereo()
#
# #August
# ax = fig.add_subplot(234)
# ax.set_title("August")
# a = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = a(lon, lat)
# a.fillcontinents(color='white',lake_color='white')
# a.drawcoastlines()
# a.drawparallels(np.arange(-80.,0.,20.))
# a.drawmeridians(np.arange(-180.,181.,20.))
# a.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# a.contourf(x,y,gs_augs,40,cmap=cmap0,levels=[0,1,2,3,4,5])
# transform=ccrs.SouthPolarStereo()
#
# #September
# ax = fig.add_subplot(235)
# ax.set_title("September")
# s = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = s(lon, lat)
# s.fillcontinents(color='white',lake_color='white')
# s.drawcoastlines()
# s.drawparallels(np.arange(-80.,0.,20.))
# s.drawmeridians(np.arange(-180.,181.,20.))
# s.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# s.contourf(x,y,gs_seps,40,cmap=cmap0,levels=[0,1,2,3,4,5])
# transform=ccrs.SouthPolarStereo()
#
# #October
# ax = fig.add_subplot(236)
# ax.set_title("October")
# oc = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = oc(lon, lat)
# oc.fillcontinents(color='white',lake_color='white')
# oc.drawcoastlines()
# oc.drawparallels(np.arange(-80.,0.,20.))
# oc.drawmeridians(np.arange(-180.,181.,20.))
# oc.drawmapboundary(fill_color='black')
# cmap0 = plt.cm.get_cmap('jet', 11)
# oc.contourf(x,y,gs_octos,40,cmap=cmap0,levels=[0,1,2,3,4,5])
# transform=ccrs.SouthPolarStereo()
#
# fig.suptitle(u'Monthly sea ice thickness \n  2003-2011', fontsize=15, y=1)
# plt.subplots_adjust(wspace=0.05, hspace=0.05, right=0.8)
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# #cbar_ax = fig.add_axes([-0.05, 0.15, 0.02, 0.7])
# cbar_axx = fig.add_axes([1, 0.15, 0.02, 0.7])
#
# fig.colorbar(clr2,cax=cbar_axx,label= u'\n Sea ice thickness (m)')
# #fig.colorbar(clr1, cax=cbar_axx,label= 'SIT (m) mean')
#
# # saving figure #
# #plt.savefig('months_sit.png', dpi=300, bbox_inches='tight')
#
# # showing figure #
# plt.show()
#

# # In[ ]:
# months=volume.groupby('time.season').mean('time', keep_attrs=True)
# months_sia=area.groupby('time.season').mean('time', keep_attrs=True)
# months_sit=sit.groupby('time.season').mean('time', keep_attrs=True)
# # In[ ]:
# JJA=months.sel(season='JJA')
# SON=months.sel(season='SON')
# MAM=months.sel(season='MAM')
# #sia
# JJA_sia=months_sia.sel(season='JJA')
# SON_sia=months_sia.sel(season='SON')
# MAM_sia=months_sia.sel(season='MAM')
# #volume
# JJA_vol=months_sit.sel(season='JJA')
# SON_vol=months_sit.sel(season='SON')
# MAM_vol=months_sit.sel(season='MAM')


# In[ ]:


# #plt.savefig('SON.png')
# import cartopy.crs as ccrs
# import cartopy.feature as cfeature
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap # plots maps
#
# fig = plt.figure(figsize=[12,10])
#
# #MAM
# ax = fig.add_subplot(131)
# ax.set_title("MAM")
# m = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = m(lon, lat)
# m.fillcontinents(color='white',lake_color='white')
# m.drawcoastlines()
# m.drawparallels(np.arange(-80.,0.,20.))
# m.drawmeridians(np.arange(-180.,181.,20.))
# m.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# clr2=m.contourf(x,y,months.sel(season='MAM'),40,cmap=cmap0,levels=[0,500,1000,1500,2000,2500,3000,3500])
# transform=ccrs.SouthPolarStereo()
#
# #JJA
# ax = fig.add_subplot(132)
# ax.set_title("JJA")
#
# j = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = j(lon, lat)
# j.fillcontinents(color='white',lake_color='white')
# j.drawcoastlines()
# j.drawparallels(np.arange(-80.,0.,20.))
# j.drawmeridians(np.arange(-180.,181.,20.))
# j.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# j.contourf(x,y,months.sel(season='JJA'),40,cmap=cmap0,levels=[0,500,1000,1500,2000,2500,3000,3500])
# transform=ccrs.SouthPolarStereo()
#
# #SON
# ax = fig.add_subplot(133)
# ax.set_title("SON")
# jj = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = jj(lon, lat)
# jj.fillcontinents(color='white',lake_color='white')
# jj.drawcoastlines()
# jj.drawparallels(np.arange(-80.,0.,20.))
# jj.drawmeridians(np.arange(-180.,181.,20.))
# jj.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# jj.contourf(x,y,months.sel(season='SON'),40,cmap=cmap0,levels=[0,500,1000,1500,2000,2500,3000,3500])
# transform=ccrs.SouthPolarStereo()
#
# #fig.suptitle(u' Sea Ice\n  2003-2011', fontsize=15, y=1)
# plt.subplots_adjust(wspace=0.05, hspace=0.05, right=0.8)
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# #cbar_ax = fig.add_axes([-0.05, 0.15, 0.02, 0.7])
# cbar_axx = fig.add_axes([1, 0.15, 0.02, 0.7])
#
# fig.colorbar(clr2,cax=cbar_axx,label= u'\n Sea ice volume (km3)')
# #fig.colorbar(clr1, cax=cbar_axx,label= 'SIT (m) mean')

# saving figure #
#plt.savefig('sit_by_season.png', dpi=300, bbox_inches='tight')


# In[ ]:


# ax=table.set_index('Dates').plot(figsize=(10,5), grid=True)
# ax.set_xlabel("Years")
# ax.set_ylabel("Sea ice volume (km3)")
#plt.savefig('Regions_volume.pdf', dpi=300, bbox_inches='tight')


# In[ ]:


#df_son_sia=SON_sia.to_dataframe


# ## SIT by season

# In[ ]:


#plt.savefig('SON.png')
import cartopy.crs as ccrs
import cartopy.feature as cfeature
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap # plots maps
#
# fig = plt.figure(figsize=[12,10])
#
# #MAM
# ax = fig.add_subplot(131)
# ax.set_title("MAM")
# m = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = m(lon, lat)
# m.fillcontinents(color='white',lake_color='white')
# m.drawcoastlines()
# m.drawparallels(np.arange(-80.,0.,20.))
# m.drawmeridians(np.arange(-180.,181.,20.))
# m.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# clr2=m.contourf(x,y,months_sit.sel(season='MAM'),40,cmap=cmap0,levels=[0,1,2,3,4,5,6])
# transform=ccrs.SouthPolarStereo()
#
# #JJA
# ax = fig.add_subplot(132)
# ax.set_title("JJA")
#
# j = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = j(lon, lat)
# j.fillcontinents(color='white',lake_color='white')
# j.drawcoastlines()
# j.drawparallels(np.arange(-80.,0.,20.))
# j.drawmeridians(np.arange(-180.,181.,20.))
# j.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# j.contourf(x,y,months_sit.sel(season='JJA'),40,cmap=cmap0,levels=[0,1,2,3,4,5,6])
# transform=ccrs.SouthPolarStereo()
#
# #SON
# ax = fig.add_subplot(133)
# ax.set_title("SON")
# jj = Basemap(projection= 'spaeqd',boundinglat=-50,lon_0=-180,resolution='l')
# x, y = jj(lon, lat)
# jj.fillcontinents(color='white',lake_color='white')
# jj.drawcoastlines()
# jj.drawparallels(np.arange(-80.,0.,20.))
# jj.drawmeridians(np.arange(-180.,181.,20.))
# jj.drawmapboundary(fill_color='lightblue')
# cmap0 = plt.cm.get_cmap('jet', 11)
# jj.contourf(x,y,months_sit.sel(season='SON'),40,cmap=cmap0,levels=[0,1,2,3,4,5,6])
# transform=ccrs.SouthPolarStereo()
#
# #fig.suptitle(u' Sea Ice\n  2003-2011', fontsize=15, y=1)
# plt.subplots_adjust(wspace=0.05, hspace=0.05, right=0.8)
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# #cbar_ax = fig.add_axes([-0.05, 0.15, 0.02, 0.7])
# cbar_axx = fig.add_axes([1, 0.15, 0.02, 0.7])
#
# fig.colorbar(clr2,cax=cbar_axx,label= u'\n Sea ice thickness (m)')
# #fig.colorbar(clr1, cax=cbar_axx,label= 'SIT (m) mean')

# saving figure #
#plt.savefig('sit_by_season.png', dpi=300, bbox_inches='tight')

