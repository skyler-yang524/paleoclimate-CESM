import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
#cartopy package is for geological configuaration plotting
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.patches import Polygon

# User defined parameters
casename = "310 Ma Annual Mean Temperature"

# Read in data
myfile = xr.open_dataset("/Path to nc file/High_Resolution_Climate_Simulation_Dataset_540_Myr.nc")
T = myfile["T"]
#LANDFRAC is for plotting the geological configuration, see function defined below
#This steps is pretty optional and it really depends on what dataset you have in your hand; the reason I did this step is because this script is basically transfered from the corresponding NCL file.
LANDFRAC = myfile["LANDFRAC"]
lat = myfile["lat"]
lon = myfile["lon"]

# Compute the annual mean temperature by averaging over the 'month' dimension
T_annual = T.mean(dim="month")

# Function to add geological configuration
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

#ax.countourf is used for plotting the countour on the plot and add_paleo_outline function is used to create the geological configuration via creating the mask.
try:
    #Cmap could be changed to anyother colors. Check matplotlib for more options.
    im = ax.contourf(lon, lat, T_annual.isel(simulation=24), levels=np.arange(-24, 44, 4), transform=ccrs.PlateCarree(), cmap="BuYlRd", extend='both')
    
    # Mask created at coordinates where the land fraction is greater than 0.5. In this case, we could place one polygon at the point.
    oro = np.where(LANDFRAC.isel(simulation=24).values > 0.5, 1, 0)
    add_paleo_outline(ax, oro, lat, lon)
    
except Exception as e:
    print(f"Failed to plot for {casename}: {e}")

# Adjust and add colorbar
fig.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.9)
cbar = fig.colorbar(im, orientation='horizontal', pad=0.05)
cbar.set_label('Temperature (°C)', fontsize=12)

plt.show()


