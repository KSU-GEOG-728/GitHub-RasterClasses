# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo13_1.py
    Author: Shawn Hutchinson
    Description:  Example script that sets the raster "mask" environment
    Date created: November 19, 2025
    Python Version: 3.11.11
"""

# Import required modules:
import arcpy, os

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
arcpy.env.overwriteOutput = True
arcpy.env.mask = "KonzaBoundary"

# Define local variable(s)
demGrid = "dem10"
outWorkspace = "D:/GitHub/GitHub-Rasters/scratch.gdb"

# Perform geoprocessing and trap errors
try:
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
        outGrid = arcpy.sa.Slope(demGrid)
        outGrid.save(os.path.join(outWorkspace, "slope10_kz1"))
        arcpy.CheckInExtension("Spatial")
    else:
        print("Required Spatial Analyst extension is not available!")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except:
    print("Warning - An unexpected error occurred...")

finally:

    print("Script ran to completion...excellent!")    
