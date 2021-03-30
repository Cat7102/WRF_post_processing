import matplotlib.pyplot as plt
import netCDF4 as nc
from wrf import getvar,ALL_TIMES,to_np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
import numpy as np

fileobj=nc.Dataset("K:\\2019-6-27-ucm\\wrfout_d03_2019-06-25_12-00-00.nc")

times=getvar(fileobj,'times',timeidx=ALL_TIMES)
times=to_np(times)
for i in range(len(times)):
    print('['+str(i)+']'+str(times[i]))

t2=to_np(getvar(fileobj,'T2',timeidx=306))
t2=t2-273.15
u10=fileobj.variables['U10'][306,:,:]
v10=fileobj.variables['V10'][306,:,:]
lat=to_np(getvar(fileobj,'lat'))
lon=to_np(getvar(fileobj,'lon'))

fig = plt.figure(figsize=(12,6),dpi=150)
proj = ccrs.PlateCarree()
axe = plt.subplot(1,1,1, projection = proj)

axe.add_feature(cfeat.COASTLINE.with_scale('10m'), linewidth=0.5, zorder=1) #海岸线
#axe.add_feature(cfeat.LAKES.with_scale('10m'), linewidth=0.5, zorder=1) #海岸线
axe.set_title('1231')

axe.set_extent([120,122.4,30,31.8], crs=proj) #设置范围

# 绘制网格
gl = axe.gridlines(
    crs=proj, draw_labels=True,
    linewidth=0.5, color='gray', linestyle='--')
# 可以控制坐标轴出现的位置，设置False表示隐藏
gl.top_labels = False
gl.right_labels = False
# 自定义给出x轴Locator的位置
gl.xlocator = mticker.FixedLocator(np.arange(120.4,122.2,0.2))
gl.ylocator = mticker.FixedLocator(np.arange(30,31.8,0.2))
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style={'size':8,"color":'black'}
gl.ylabel_style={'size':4.5,'color':'red'}

ac=axe.contourf(lon,lat,t2,levels=np.arange(18,33,1),cmap=plt.get_cmap('jet'))
cb = fig.colorbar(ac,spacing='proportional')

u=u10[::4,::4]
v=v10[::4,::4]
lon=lon[::4,::4]
lat=lat[::4,::4]
axe.quiver(lon, lat, u, v, pivot='mid',
                width=0.0015, scale=200, color='black', headwidth=5,
                transform=ccrs.PlateCarree())

fig.show()
plt.show()