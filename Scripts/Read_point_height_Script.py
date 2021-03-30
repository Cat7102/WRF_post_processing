from wrf import getvar,to_np,ll_to_xy
import netCDF4 as nc

ncfile=nc.Dataset("F:/wrfout_d03_2016-07-21_00_00_00.nc") #这里改下路径
lon=to_np(getvar(ncfile,'lon'))
lat=to_np(getvar(ncfile,'lat'))

point_lat,point_lon=30,122 #这里改你的纬度和经度

y,x=ll_to_xy(ncfile,point_lat,point_lon)
print("最近点的索引：")
print(x.values,y.values)
print("最近点的经纬度：")
print(lon[x,y],lat[x,y])

hgt=ncfile.variables['HGT'][0,x,y]
height=to_np(getvar(ncfile,"height"))[:,x,y]
print(height.shape)

print("该层的海拔高度、离地高度和地面层海拔高度分别是：")
for i in range(height.shape[0]):
	print("["+str(i)+"]"+str(height[i])+" , "+str(height[i]-hgt)+" , "+str(hgt))
