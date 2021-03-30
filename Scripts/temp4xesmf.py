#这个脚本用于绘制平面图，各个功能按需自行删除注释

import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import xesmf as xe
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import matplotlib.ticker as mticker
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cmaps
from wrf import getvar, to_np, ALL_TIMES

#读取文件及数据
xrfile=xr.open_dataset('/media/fishercat/Data,Doc,Recourse etc/wrfout_d03_2016-07-21_00_00_00.nc')
ncfile=nc.Dataset('/media/fishercat/Data,Doc,Recourse etc/wrfout_d03_2016-07-21_00_00_00.nc')
xr2lat=xrfile.coords['XLAT'].isel(Time=0).values.tolist()
xr2lon=xrfile.coords['XLONG'].isel(Time=0).values.tolist()
#print(xr2lat)
xr2=xr.Dataset(coords={'latitude':(["south_north","west_east"],xr2lat),'longitude':(["south_north","west_east"],xr2lon)})
t2=xrfile['T2'].isel(Time=0)
t2=t2.rename({"XLAT":'latitude',"XLONG":"longitude"})

#t2_grid=t2.rename({"lat":'longitude',"lon":"latitude"})

#t2_grid=t2_grid.assign_coords(longitude=t2.lon,latitude=t2.lat)
#print(t2_grid)

grid_out=xe.util.grid_2d(122,123,1,31,32,1)
#print(xr2)
print(grid_out)
ret2=xe.Regridder(xr2,grid_out,'nearest_s2d')
t2out=ret2(t2)
print(t2out)

