import os,sys
import xarray as xr 
import pandas as pd 
import matplotlib.pyplot as plt
#import netCDF4 as nc


fn  = sys.argv[1]
var = sys.argv[2]

#fn = 'A2082800.nc'
fb = fn.split(".")[0]

gn = '%s_%s.png' % (fb, var)
ds = xr.open_dataset(fn)
print(list(ds.keys()))

sys.exit()

fig, ax = plt.subplots(figsize=(10,6))
back = ds[var]
back = back.T
back.plot(ax=ax)
plt.savefig(gn)
plt.show()
plt.close()

#back = ds['backscatter'][:,:]
#plt.figure(figsize=(10,10))
#plt.imshow(back,origin='lower') 
#plt.show()

