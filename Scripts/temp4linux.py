import netCDF4 as nc

file_path="/home/fishercat/Build_WRF/prep_chem_sources_1.5/bin/Global_emissions_v3/Emission_data/GOCART/dms_data/dms_1x1.25.nc"
file_obj=nc.Dataset(file_path)


print(file_obj.variables.keys())
print(file_obj.variables['time'])