# Paleoclimate simulation using Community Earth System Model(CESM)
The `Visualization` folder contains code for plot visualization using Python with model output in netCDF files. For more detailed information on how to convert NCL files to Python scripts for model visualization, see (https://www.zhihu.com/column/c_1377048729833291776).
## Installing, building and running CESM
See CESM github page for detail instruction: https://github.com/ESCOMP/CESM?tab=readme-ov-file#id1. CESM source code could be downloaded: https://github.com/ESCOMP/CESM/releases; you may find newest released version to download.
## CESM tutorial: practical and lectures
"NCAR provides an annual CESM tutorial that covers both the conceptual framework of CESM and its practical applications. Tutorials for each year can be found [here](https://www2.cesm.ucar.edu/events/tutorials/). I personally watched the 2020 tutorial, available [here](https://www2.cesm.ucar.edu/events/tutorials/2020/coursework.html); both slides and recordings can be found at the link.

## CESM porting to Niagara
The detailed instructions for installing and porting CESM to Niagara can be found on this GitHub page[here](https://github.com/JohnVirgin/CESM-Niagara) . These instructions are relatively easier to follow compared to the NCAR CESM webpage.

However, please note that the config_* files on this GitHub page might be somewhat outdated. When I used the setup from this page, I encountered a "Segmentation Fault" error when trying to run the coupled complex model.

The updated config_* files I used for Niagara can be found [here](https://github.com/skyler-yang524/paleoclimate-CESM/tree/main/Niagara%20porting). A big thank you to Noah for providing the config_* file setup for Niagara. I have also indicated which parts of the config files were edited for the complex model run from the Github Niagara-CESM page. 

## CESM1 run for paleo-period simulation
### Porting of CESM1
CESM1 installation package could be found in the NCAR CESM1 user guide: [here](https://www2.cesm.ucar.edu/models/cesm1.2/cesm/doc/usersguide/ug.pdf). According to the user guide instructions, you should download the latest version (I used CESM1.2.2 and CESM1.2.2dt). CESM1.2.2dt stands for the deep time. However, note that several libraries used in CESM1 are now outdated, and some of the GitHub links required for installation are no longer available. My solution in this step is when i encountered the error line of something couldnt be downloaded, I found the resources link online and manually installed them. Just keep in mind that CESM1 is quite old, and many components are no longer supported.
### Config Files
Specific config files for Niagara could also be found from my the above porting step. Make sure you edit your own path. You can either download my revised version: [cesm1.2.2](https://github.com/skyler-yang524/paleoclimate-CESM/tree/main/CESM1.2.2)/ [cesm1.2.2dt](https://github.com/skyler-yang524/paleoclimate-CESM/tree/main/cesm1.2.2dt), which has been modified for easier porting, or make your own adjustments. Just keep in mind that Niagara is not one of the supported machine for CESM to run, so you need to modify the setup files by yourself.
### Notes on CESM1.2.2dt 
CESM1.2.2 Deep Time is based on the standard CESM1.2.2 framework but lacks many essential input files, such as topography and grid setup files. This is because the continental configurations during deep-time periods differ significantly from the present-day land-ocean distribution. Therefore, you will need to create your own initial setup files. The [Paleoclimate Toolkit](https://www.cesm.ucar.edu/models/paleo) provided by NCAR serves as a great starting point for this process.
