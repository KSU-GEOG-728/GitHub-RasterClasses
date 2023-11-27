#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo13_2.py
    Author: Shawn Hutchinson
    Description:  Example script that sets the raster "mask" and "extent" environments
    Date created: November 27, 2023
    Python Version: 3.9.16
"""

# Import required modules and classes:
import arcpy, os
from arcpy import env
from arcpy.sa import *


# Set environment(s)
env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
env.overwriteOutput = True
env.mask = "KonzaBoundary"
env.extent = "KonzaBoundary"

# Define local variable(s)
demGrid = "dem10"
outWorkspace = "D:/GitHub/GitHub-Rasters/scratch.gdb"

# Perform geoprocessing and trap errors
try:
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
        outGrid = Slope(demGrid)
        outGrid.save(os.path.join(outWorkspace, "slope10_kz2"))
        arcpy.CheckInExtension("Spatial")
    else:
        print("Required Spatial Analyst extension is not available!")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except:
    print("Warning - An unexpected error occurred...")

finally:
    print("Script ran to completion...excellent!")        