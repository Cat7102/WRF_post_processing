#这个脚本用于绘制平面图，各个功能按需自行删除注释

import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import matplotlib.ticker as mticker
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cmaps
from wrf import getvar, to_np, ALL_TIMES
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun'
mpl.rcParams['axes.unicode_minus']=False

#1.读取文件及数据
################################################################################################################
ncfile=nc.Dataset('F:/wrfout_d01_2016-07-21_00_00_00.nc')
lon=getvar(ncfile,'lon')
lat=getvar(ncfile,'lat')
t2_28=getvar(ncfile,'T2',timeidx=28)
t2_28=t2_28-273.15 #t2变量要记得单位是K
rh2_28=getvar(ncfile,'rh2',timeidx=28)
u10_28=ncfile.variables['U10'][28,:,:]
v10_28=ncfile.variables['V10'][28,:,:]
t2_32=getvar(ncfile,'T2',timeidx=32)
t2_32=t2_32-273.15 #t2变量要记得单位是K
rh2_32=getvar(ncfile,'rh2',timeidx=32)
u10_32=ncfile.variables['U10'][32,:,:]
v10_32=ncfile.variables['V10'][32,:,:]
################################################################################################################

#2.画布初始化
################################################################################################################
proj=ccrs.PlateCarree()#定义气象图的布局
fig=plt.figure(figsize=(10,8),dpi=150)
#第一个子图
############################################################################
axe_1=plt.subplot(1,2,1,projection=proj) #这里可以设置多个子图，第一个参数表示多少行，第二个表示多少列，第三个表示第几个子图
axe_1.set_title("20160722 12:00:00",fontsize=12)
#添加海岸线数据
axe_1.add_feature(cfeat.COASTLINE.with_scale('10m'),linewidth=0.7)
#通过下面两行代码可以添加湖泊轮廓线，其他的以此类推
LAKES_border=cfeat.NaturalEarthFeature('physical','lakes','10m',edgecolor='black',facecolor='never')
axe_1.add_feature(LAKES_border,linewidth=1)
#axe_1.add_feature(cfeat.OCEAN.with_scale('10m'))
axe_1.set_extent([100-0.1,140.1,15-0.1,45.1],crs=proj) #设置可视化的范围，采用加个0.1的方式是为了让坐标显示全
# 绘制网格
gl = axe_1.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=0.7, color='gray', linestyle=':')
# 可以控制坐标轴出现的位置，设置False表示隐藏
gl.top_labels = False
#gl.bottom_labels = False
gl.right_labels = False
#gl.left_labels = False
# 自定义给出x轴Locator的位置
gl.xlocator = mticker.FixedLocator(np.arange(120, 122.5, 0.5))
gl.ylocator = mticker.FixedLocator(np.arange(30, 32.5, 0.5))
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style={'size':8,"color":'black'}
gl.ylabel_style={'size':8,'color':'black'}
#下面的用于设置minor刻度，不需要就注释掉
axe_1.set_xticks(np.arange(120, 122, 0.1), crs=proj, minor=True)
axe_1.set_yticks(np.arange(30, 32, 0.1), crs=proj, minor=True)
plt.xticks([])
plt.yticks([])
#第二个子图
############################################################################
axe_2=plt.subplot(1,2,2,projection=proj) #这里可以设置多个子图，第一个参数表示多少行，第二个表示多少列，第三个表示第几个子图
axe_2.set_title("20160722 16:00:00",fontsize=12)
#添加海岸线数据
axe_2.add_feature(cfeat.COASTLINE.with_scale('10m'),linewidth=0.7)
#通过下面两行代码可以添加湖泊轮廓线，其他的以此类推
LAKES_border=cfeat.NaturalEarthFeature('physical','lakes','10m',edgecolor='black',facecolor='never')
axe_2.add_feature(LAKES_border,linewidth=1)
#axe_1.add_feature(cfeat.OCEAN.with_scale('10m'))
axe_2.set_extent([120-0.1,122.1,30-0.1,32.1],crs=proj) #设置可视化的范围，采用加个0.1的方式是为了让坐标显示全
# 绘制网格
gl = axe_2.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=0.7, color='gray', linestyle=':') #color='none'是透明网格
# 可以控制坐标轴出现的位置，设置False表示隐藏
gl.top_labels = False
#gl.bottom_labels = False
gl.right_labels = False
#gl.left_labels = False
# 自定义给出x轴Locator的位置
gl.xlocator = mticker.FixedLocator(np.arange(120, 122.5, 0.5))
gl.ylocator = mticker.FixedLocator(np.arange(30, 32.5, 0.5))
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style={'size':8,"color":'black'}
gl.ylabel_style={'size':8,'color':'black'}
#下面的用于设置minor刻度，不需要就注释掉
axe_2.set_xticks(np.arange(120, 122, 0.1), crs=proj, minor=True)
axe_2.set_yticks(np.arange(30, 32, 0.1), crs=proj, minor=True)
plt.xticks([])
plt.yticks([])
############################################################################
################################################################################################################

#3.填充等高线颜色
################################################################################################################
level_t2=np.arange(25, 38, 0.3)
#cmap的填充色可以看附图自己修改
contourf_1 = axe_1.contourf(lon, lat, t2_28,levels=level_t2,cmap=cmaps.NCV_rainbow2)
contourf_2 = axe_2.contourf(lon, lat, t2_32,levels=level_t2,cmap=cmaps.NCV_rainbow2)
print("最大和最小的温度分别是：")
print(np.max(t2_28).values,np.min(t2_28).values)
print(np.max(t2_32).values,np.min(t2_32).values)
################################################################################################################

#4.绘制等高线轮廓
################################################################################################################
level_rh2=np.arange(50,100,10)
#linestyles可以设置solid
contour_1 = axe_1.contour(lon, lat, rh2_28, levels=level_rh2, colors='white',linewidths=1, linestyles='dashed')
axe_1.clabel(contour_1, inline=True, fontsize=8, colors='white',fmt='%1.0f')
contour_2 = axe_2.contour(lon, lat, rh2_32, levels=level_rh2, colors='white',linewidths=1, linestyles='dashed')
axe_2.clabel(contour_2, inline=True, fontsize=8, colors='white',fmt='%1.0f')
################################################################################################################

#5.绘制矢量箭头图
################################################################################################################
u10_28x, u10_32x = u10_28[::2, ::2], u10_32[::2, ::2]
v10_28x, v10_32x = v10_28[::2, ::2], v10_32[::2, ::2]
latx, lonx = lat[::2, ::2], lon[::2, ::2]
q_1=axe_1.quiver(lonx, latx, u10_28x, v10_28x, pivot='mid',
             width=0.0018, scale=180, color='black', headwidth=3,
             transform=ccrs.PlateCarree())
#绘制矢量箭头的图例
axe_1.quiverkey(q_1,0.9,1.02,4,'4m/s',labelpos='E',coordinates='axes',fontproperties={'size':8})
q_2=axe_2.quiver(lonx, latx, u10_32x, v10_32x, pivot='mid',
             width=0.0018, scale=180, color='black', headwidth=3,
             transform=ccrs.PlateCarree())
axe_2.quiverkey(q_2,0.9,1.02,4,'4m/s',labelpos='E',coordinates='axes',fontproperties={'size':8})
################################################################################################################

#6.绘制图例
################################################################################################################
rect = [0.2, 0.1, 0.6, 0.03]  # 分别代表，水平位置，垂直位置，水平宽度，垂直宽度
cbar_ax = fig.add_axes(rect)
cb = fig.colorbar(contourf_1, cax=cbar_ax, orientation='horizontal',spacing='proportional')  # orientation='vertical'
cb.set_label("温度坐标(℃)")
################################################################################################################

#7.调整子图间距
################################################################################################################
plt.subplots_adjust(wspace=0.3,hspace=0.1)
################################################################################################################

#最后一步，展示图像
fig.show()
plt.show()

