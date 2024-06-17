
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Polygon

# User defined parameters
casename = "310 Ma Annual Mean Temperature"

# Read in data
myfile = xr.open_dataset("/Users/yangduo/Downloads/19920662/High_Resolution_Climate_Simulation_Dataset_540_Myr.nc")
T = myfile["T"]
LANDFRAC = myfile["LANDFRAC"]
lat = myfile["lat"]
lon = myfile["lon"]

# Compute the annual mean temperature by averaging over the 'month' dimension
T_annual = T.mean(dim="month")

# Function to add paleo outlines
def add_paleo_outline(ax, oro, lat, lon):
    for i in range(len(lat)):
        for j in range(len(lon)):
            if oro[i, j]:
                polygon = Polygon([(lon[j].item() - 0.5, lat[i].item() - 0.5), 
                                   (lon[j].item() + 0.5, lat[i].item() - 0.5), 
                                   (lon[j].item() + 0.5, lat[i].item() + 0.5), 
                                   (lon[j].item() - 0.5, lat[i].item() + 0.5)], 
                                  closed=True, edgecolor='White', facecolor='none', transform=ccrs.PlateCarree())
                ax.add_patch(polygon)

# Set up the plot
fig, ax = plt.subplots(figsize=(15, 9), subplot_kw={'projection': ccrs.Mollweide()})

print(f"Processing case: {casename}")

# Plot
ax.set_title(f"{casename}", fontsize=10)
#ax.coastlines()

try:
    im = ax.contourf(lon, lat, T_annual.isel(simulation=24), levels=np.arange(-24, 44, 4), transform=ccrs.PlateCarree(), cmap="RdYlBu", extend='both')
    
    # Mask
    oro = np.where(LANDFRAC.isel(simulation=24).values > 0.5, 1, 0)
    add_paleo_outline(ax, oro, lat, lon)
    
except Exception as e:
    print(f"Failed to plot for {casename}: {e}")

# Adjust and add colorbar
fig.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.9)
cbar = fig.colorbar(im, orientation='horizontal', pad=0.05)
cbar.set_label('Temperature (°C)', fontsize=12)

plt.show()


