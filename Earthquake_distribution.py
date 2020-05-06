#!  python3

"""
Plotting the earthquakes in the area 
- For the receent active area (small area)
- For the longerr time period from old catalog

@ Author: Roshan Koirala
"""

#================================================================================
#                          Modules
#================================================================================  
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#================================================================================
#                          Plotting The Earthquakes around  4.8 ML 
#================================================================================ 
fig = plt.figure(figsize=(10, 10))
map = Basemap(llcrnrlat=31.65,urcrnrlat=31.74,llcrnrlon=-104.1,urcrnrlon=-104.,
              projection='tmerc', lat_1=31.67, lat_2=32, lat_0=31, lon_0=-104.05, resolution='c')

map.drawstates(color='black' )
map.drawlsmask(land_color='0.8', grid=5,lakes=True)
map.drawrivers(color='navy')
map.drawparallels(np.arange(31.66, 31.74, 0.02),labels = (False,True,False,True))
map.drawmeridians(np.arange(-104.08, -104, 0.02),labels = (False,True,False,True))

# plot earthquakes
df = pd.read_csv('texnet_events.csv')
tx_lat = df['Lat'].tolist()
tx_lon = df['Lon'].tolist()
magnitude = df['Mag'].tolist()
depth = df['Depth'].tolist()

x,y = map(tx_lon,tx_lat)
map.scatter(x, y, s=60, c=depth)
c = plt.colorbar(orientation='horizontal', fraction=0.044, pad=0.05)
c.set_label("Depth")

df = pd.read_csv('Well_location.csv')
well_lat = df['Lat'].tolist()
well_lon = df['Lon'].tolist()
well_depth = df['Depth'].tolist()

map.scatter( well_lon,well_lat,label='Wells ',  latlon=True, s=100, color='r', marker='s', alpha=1, edgecolor='k', zorder=4)


map.scatter(-104.0519,31.7033,label='4.8 ML | 6.0 KM ',  latlon=True, s=400, marker='*', alpha=1, edgecolor='k', zorder=3)
plt.title('Earthquake Around the 4.8 ML Epicenter (2018 - Date)', fontweight="bold")
plt.legend(loc='lower right')
plt.savefig("Eq_around_epi.png", dpi=500)
plt.show()

#================================================================================
#                          Plotting The Earthquakes For Bigger area
#================================================================================ 
fig = plt.figure(figsize=(12, 12))
map = Basemap(llcrnrlat=29.0,urcrnrlat=34.0,llcrnrlon=-107.0,urcrnrlon=-98.0,
              projection='tmerc', lat_1=31.00, lat_2=33.00, lat_0=31, lon_0=-104.05, resolution='c')

map.drawstates(color='red', linewidth = 3)
map.drawlsmask(land_color='lightgrey', grid=5,lakes=True)
map.drawrivers(color='navy')
map.drawparallels(np.arange(30., 34., 1.),labels = (False,True,False,True))
map.drawmeridians(np.arange(-107., -98, 1.),labels = (False,True,False,True))

# plot earthquakes
df = pd.read_csv('All_catalog.csv')
tx_lat = df['Lat'].tolist()
tx_lon = df['Lon'].tolist()


x,y = map(tx_lon,tx_lat)
map.scatter(x, y, s=10, label='Earthquakes',)
map.scatter(-104.0519,31.7033,label='4.8 ML',  latlon=True, s=400, marker='*', alpha=1, edgecolor='k', zorder=3)
plt.title('Earthquake Distribution - West Texas (2000 - 2017)', fontweight="bold")
plt.legend(loc='lower right')
plt.savefig("Eq_all.png", dpi=500)
plt.show()

