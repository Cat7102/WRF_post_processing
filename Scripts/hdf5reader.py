import h5py
import numpy as np

h5file=h5py.File('/home/fishercat/Build_WRF/prep_chem_sources_1.5/bin/Global_emissions_v4/Emission_data/EDGARV5/EDGAR_2005.h5')

print(h5file.keys())
print(h5file['STATIONARY_SOURCES'])