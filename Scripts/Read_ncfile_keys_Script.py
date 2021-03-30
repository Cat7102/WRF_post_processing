import netCDF4 as nc

ncfile=nc.Dataset("E:/chem_data/mozart4geos5-global-20160720-30.nc") #这里改路径

n=1

for i in ncfile.variables.keys():
    print(i,end=',')
    n += 1
    if n%10 ==0:
        print()