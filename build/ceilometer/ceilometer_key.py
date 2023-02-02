import xarray as xr
import pandas as pd

fn = 'A2082800.nc'
ds = xr.open_dataset(fn)
values = list(ds.keys())
with open("ceilometer_keys.txt", "w") as output:
    output.write(str(values))