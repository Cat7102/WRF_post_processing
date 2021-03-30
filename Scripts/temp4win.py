import xarray as xr
import netCDF4 as nc
from wrf import getvar,to_np,xy_to_ll,ll_to_xy
import numpy as np

ncfile=nc.Dataset("E:/chem_data/mozart4geos5-global-20160720-30.nc") #这里改路径
time=ncfile.variables['datesec']
print(time.shape)
c3h6=ncfile.variables['C3H6_VMR_inst']
print(c3h6.shape)

