# Paleoclimate simulation using Community Earth System Model(CESM)
The `Visualization` folder contains code for plot visualization using Python with model output in netCDF files. For more detailed information on how to convert NCL files to Python scripts for model visualization, see (https://www.zhihu.com/column/c_1377048729833291776).
## Installing, building and running CESM
See CESM github page for detail instruction: https://github.com/ESCOMP/CESM?tab=readme-ov-file#id1. CESM source code could be downloaded: https://github.com/ESCOMP/CESM/releases; you may find newest released version to download.
## CESM tutorial: practical and lectures
"NCAR provides an annual CESM tutorial that covers both the conceptual framework of CESM and its practical applications. Tutorials for each year can be found [here](https://www2.cesm.ucar.edu/events/tutorials/). I personally watched the 2020 tutorial, available [here](https://www2.cesm.ucar.edu/events/tutorials/2020/coursework.html); both slides and recordings can be found at the link.

## CESM porting to Niagara
The detailed instructions for installing and porting CESM to Niagara can be found on this GitHub page[here](https://github.com/JohnVirgin/CESM-Niagara) . These instructions are relatively easier to follow compared to the NCAR CESM webpage.

However, please note that the config_* files on this GitHub page might be somewhat outdated. When I used the setup from this page, I encountered a "Segmentation Fault" error when trying to run the coupled complex model.

The updated config_* files I used for Niagara can be found [here](). A big thank you to Noah for providing the config_* file setup for Niagara. I have also indicated which parts of the config files were edited for the complex model run from the Github Niagara-CESM page. 
