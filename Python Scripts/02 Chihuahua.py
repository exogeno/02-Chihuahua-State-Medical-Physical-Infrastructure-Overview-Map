# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:57:11 2021

@author: JOSECAL
"""

import geopandas  as gpd
import matplotlib.pyplot as plt
import pysal as ps
import warnings
import numpy as np
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon
from geopandas import GeoDataFrame, GeoSeries
from geopandas.array import _check_crs, _crs_mismatch_warn
from pyproj import Proj, transform


# Importing an ESRI Shapefile and plotting it using GeoPandas
estado_02 = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\02 Chihuahua\Shapes\Limite estatal\lim_estatal.shp')
municipios_02=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\02 Chihuahua\Shapes\Limite municipal\lim_mun.shp')
vias_02=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\02 Chihuahua\Shapes\Vias\vias.shp')
hospitales_02=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\02 Chihuahua\Shapes\Hospitales\hospitales.shp')
anp_02=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\02 Chihuahua\Shapes\ANP\ANP.shp')

vias_mexico=gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\00 Mexico\Shapes\Vias\viassct012gw\viassct012gw.shp')

#Plotting shapefile
estado_02.plot()
municipios_02.plot()
vias_02.plot()
hospitales_02.plot()
anp_02.plot()
vias_mexico.plot()

#Plot the figures side by side
fig, (ax1, ax2) = plt.subplots(ncols= 2, figsize=(10,8))
municipios_02.plot(ax = ax1, cmap = 'magma', edgecolor = 'black', column = 'NOM_MUN')
estado_02.plot(ax = ax2, color = 'green')

#Creating a legend
fig, ax = plt.subplots(1, 1)
municipios_02.plot(column='Area', ax=ax, legend=True,
legend_kwds={'label': "Area", 'orientation': "horizontal"})


# Reprojecting GeoPandas GeoDataFrames
estado_02 = estado_02.to_crs(epsg = 32614)
municipios_02 = municipios_02.to_crs(epsg = 32614)
vias_02 = vias_02.to_crs(epsg = 32614)
hospitales_02 = hospitales_02.to_crs(epsg = 32614)
anp_02 = anp_02.to_crs(epsg = 32614)

#Plotting shapefile
estado_02.plot()
municipios_02.plot()
vias_02.plot()
hospitales_02.plot()
anp_02.plot()

# Intersecting Layers
municipios_en_anp_02 = gpd.overlay(municipios_02, anp_02, how = 'intersection')
municipios_en_anp_02.plot(color='green', edgecolor = 'red')

# Plotting multiple layers 1
fig, ax = plt.subplots(figsize = (60,40))
municipios_02.plot(ax = ax, color = 'black', edgecolor = 'white', zorder=1)
municipios_en_anp_02.plot(ax = ax, color='green', edgecolor = 'red',zorder=2, linewidth=5, alpha=0.6)

# Plotting multiple layers 2
fig, ax = plt.subplots(figsize = (40,20))
municipios_02.plot(ax = ax, color = 'black', edgecolor = 'white', zorder=2)
estado_02.plot(ax = ax, color = 'none', edgecolor = 'red',zorder=6, linewidth=3)
hospitales_02.plot(ax = ax, color = 'cyan',edgecolor = 'yellow', markersize = 130, zorder=6)
vias_02.plot(ax = ax, color = 'yellow',zorder=6, linewidth=0.5)
anp_02.plot(ax = ax, color = 'green', edgecolor = 'magenta', zorder=3)
municipios_en_anp_02.plot(ax = ax, color='none', edgecolor = 'white',zorder=4)

vias_chihuahua = gpd.clip(vias_mexico, estado_02)
vias_chihuahua.plot()






