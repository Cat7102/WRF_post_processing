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
from scipy.interpolate import griddata
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimSun'
mpl.rcParams['axes.unicode_minus']=False

# 将数据插值到网格
def ver_griddata(ncfile,varstr, time, lat_or_lon,xi,yi):
    # 指定参数类型
    factor = to_np(getvar(ncfile, varstr, timeidx=time))
    lon = to_np(getvar(ncfile, 'lon'))
    lat = to_np(getvar(ncfile, 'lat'))
    x_list, y_list, factor_list_x, factor_list = [], [], [], []
    if lat_or_lon == 0:  # 0表示沿着纬度线进行剖切
        for i in lon:
            for j in i:
                x_list.append(j)
        for i in lat:
            for j in i:
                y_list.append(j)
    if lat_or_lon == 1:  # 1表示沿着经度线进行剖切
        for i in lat:
            for j in i:
                x_list.append(j)
        for i in lon:
            for j in i:
                y_list.append(j)
    x_y = list(zip(x_list, y_list))
    for i in range(factor.shape[0]):
        for j in factor[i]:
            for k in j:
                factor_list_x.append(k)
        factor_new = griddata(x_y, factor_list_x, (xi, yi), method='cubic')  # 进行插值
        factor_list.append(factor_new)
        factor_list_x = []
    return factor_list

#不要修改
def judge4streamplt(pressure,start_p,end_p):
    start_layer,end_layer=None,None
    for i in range(pressure.shape[0]):
        if pressure[:,0][i]<end_p:#end_p设置的是大的气压，具体原因是坐标轴的设置于相反的问题
            start_layer=i-1
            break
    for i in range(pressure.shape[0]):
        if pressure[:,0][i]<start_p:#start_p设置的是小i的气压，具体原因是坐标轴的设置于相反的问题
            end_layer=i
            break
    print('原压力为：')
    print(pressure[:,0])
    bool=np.allclose(np.diff(pressure[:,0][start_layer:end_layer+1]),
                     (pressure[:,0][start_layer:end_layer+1][-1]-pressure[:,0][start_layer:end_layer+1][0])/(end_layer-start_layer+1))
    print('展示两数之差：')
    print(np.diff(pressure[:,0][start_layer:end_layer+1]))
    print((pressure[:,0][start_layer:end_layer+1][-1]-pressure[:,0][start_layer:end_layer+1][0])/(end_layer-start_layer+1))
    return bool,start_layer,end_layer

#不要修改
def griddata4streamplot(hor_ws,w,x,pressure,startlayer,endlayer,start_x,end_x,x_grid):
    x_list=[]
    for i in range(pressure.shape[0]):
        for j in x:
            x_list.append(j)
    pressure_list=[]
    for i in pressure:
        for j in i:
            pressure_list.append(j)
    #print(len(x_list))
    #print(len(pressure_list))
    x_y=list(zip(x_list,pressure_list))
    hor_ws_list,w_list=[],[]
    for i in hor_ws:
        for j in i:
            hor_ws_list.append(j)
    for i in w:
        for j in i:
            w_list.append(j)
    xi,yi=np.mgrid[start_x:end_x:complex(str(x_grid) + 'j'),
          pressure[:,0][startlayer]:pressure[:,0][endlayer]:complex(str(endlayer-startlayer+1)+'j')]
    grid_horws=griddata(x_y,hor_ws_list,(xi, yi), method='cubic')
    print('网格化的horws形状为：'+str(grid_horws.T.shape))
    grid_w = griddata(x_y, w_list, (xi, yi), method='cubic')
    print('网格化的w形状为：'+str(grid_w.T.shape))
    grid_pressure=np.mgrid[pressure[:,0][startlayer]:pressure[:,0][endlayer]:complex(str(endlayer-startlayer+1)+'j')]
    print('网格化的pressure：')
    print(grid_pressure)
    return grid_horws.T,grid_w.T,grid_pressure

#1.读取文件及数据
################################################################################################################
ncfile=nc.Dataset('F:/wrfout_d03_2016-07-21_00_00_00.nc')
lon=getvar(ncfile,'lon')
lat=getvar(ncfile,'lat')
time=28
tc=getvar(ncfile,'tc',timeidx=time)
ua=getvar(ncfile,'ua',timeidx=time)
va=getvar(ncfile,'va',timeidx=time)
wa=getvar(ncfile,'wa',timeidx=time)
pressure=getvar(ncfile,'pressure')
################################################################################################################

#2.画布初始化
################################################################################################################
proj=ccrs.PlateCarree()#定义气象图的布局
fig=plt.figure(figsize=(12,8),dpi=150)
#第一个子图
############################################################################
axe_1=plt.subplot(1,1,1) #这里可以设置多个子图，第一个参数表示多少行，第二个表示多少列，第三个表示第几个子图
axe_1.set_title("testtime",fontsize=12)
start_x, end_x=120,122
print("最大气压和最小气压（hPa）：")
start_p, end_p=500,950
big_interval_x,small_interval_x,big_interval_p,small_interval_p=0.5,0.1,50,10
axe_1.set_xlim(start_x, end_x)
axe_1.set_ylim(start_p, end_p)  # 设置图的范围
# 绘制网格
axe_1.set_xticks(np.arange(start_x, end_x +big_interval_x, big_interval_x))
axe_1.set_xticks(np.arange(start_x, end_x, small_interval_x), minor=True)
axe_1.set_yticks(np.arange(start_p, end_p + big_interval_p, big_interval_p))
axe_1.set_yticks(np.arange(start_p, end_p, small_interval_p), minor=True)
axe_1.grid(color='gray', linestyle=':', linewidth=0.7)
axe_1.invert_yaxis()#翻转纵坐标
plt.xticks(fontsize=8, color='black')  # 这一行代码用于修改刻度的字体
plt.yticks(fontsize=8, color='black')  # 这一行代码用于修改刻度的字体
# 这里添加一个xi,yi,xlist以供后面的需要
xi, yi = np.mgrid[start_x:end_x:complex(str(100) + 'j'), 31.25:31.25:1j]
xi = [row[0] for row in xi]
yi = [row[0] for row in yi]
axe_1.xaxis.set_major_formatter(LongitudeFormatter())
################################################################################################################

#2.绘制填充
################################################################################################################
pressure_grid = ver_griddata(ncfile, 'pressure', time, 0,xi,yi)
# 由于xi只有一维的信息，而其他都是二维的，所以xi也要变成二维的
x_list = []
for i in range(len(pressure_grid)):
    x_list.append(xi)
factor = ver_griddata(ncfile, 'tc', time, 0,xi,yi)
print('填充插值处理完毕')
print("计算的填充变量最小与最大值分别是：")
print(np.min(factor),np.max(factor))
level=np.arange(-50, 35, 0.3)
contourf = axe_1.contourf(x_list, pressure_grid, factor,levels=level,cmap=cmaps.NCV_rainbow2)
################################################################################################################

#3.绘制箭头
################################################################################################################
hor_ws = ver_griddata(ncfile, 'ua', time, 0,xi,yi)
w = ver_griddata(ncfile, 'wa', time, 0,xi,yi)
pressure_q = ver_griddata(ncfile, 'pressure', time, 0,xi,yi)
interval=2
hor_ws, w = np.array(hor_ws)[::interval, ::interval], np.array(w)[::interval, ::interval]
x_list, pressure_q = np.array(x_list)[::interval, ::interval], np.array(pressure_q)[::interval, ::interval]
print("x_list的结构：")
print(np.array(x_list).shape)
print("气压的结构：")
print(np.array(pressure_q).shape)
print("风速的结构：")
print(np.array(hor_ws).shape)
axe_1.quiver(x_list, pressure_q, hor_ws, w, pivot='mid',
                width=0.002, scale=350, color='black', headwidth=2)
print('箭头绘制完毕')
################################################################################################################

#3.绘制流线
################################################################################################################
hor_ws = ver_griddata(ncfile, 'ua', time, 0,xi,yi)
w = ver_griddata(ncfile, 'wa', time, 0,xi,yi)
pressure_q = ver_griddata(ncfile, 'pressure', time, 0,xi,yi)
hor_ws4sp, w4sp, pressure4sp = np.array(hor_ws), np.array(w), np.array(pressure_q)
bool, startlayer, endlayer = judge4streamplt(pressure4sp,start_p,end_p)
if bool == True:
    grid_pressure = pressure4sp[:, 0][startlayer:endlayer + 1]
    grid_horws = hor_ws[startlayer:endlayer + 1, :]
    grid_w = w[startlayer:endlayer + 1, :]
    print("将使用原数据绘制流线")
    print(grid_pressure.shape, grid_horws.shape, grid_w.shape)
if bool == False:
    grid_horws, grid_w, grid_pressure = griddata4streamplot(hor_ws, w,xi, pressure4sp, startlayer, endlayer,start_x,end_x,100)
    print("将使用网格化数据绘制流线")
    print(grid_pressure.shape)
####这里必须要做个说明！！！由于streamplot函数并不接受非线性的网格，他只接受方方正正的网格数据，因此这里必须要做一些简化操作，
####比如压力认为第一列就等效于全部。
print(np.array(xi))
axe_1.streamplot(np.array(xi), grid_pressure, grid_horws, grid_w, density=1,
                    color='blue', linewidth=1, arrowsize=1,
                    arrowstyle='-|>')

################################################################################################################

#4.绘制图例
################################################################################################################
rect = [0.92, 0.15, 0.02, 0.7]  # 分别代表，水平位置，垂直位置，水平宽度，垂直宽度
cbar_ax = fig.add_axes(rect)
cb = fig.colorbar(contourf, cax=cbar_ax, orientation='vertical',spacing='proportional')  # orientation='vertical'
cb.set_label("温度坐标(℃)")
################################################################################################################

fig.show()
plt.show()