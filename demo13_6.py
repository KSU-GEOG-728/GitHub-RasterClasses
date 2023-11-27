#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo13_6.py
    Author: Shawn Hutchinson
    Description: Example script that reclassifies a raster using a remap range class
    Date created: November 27, 2023
    Python Version: 3.9.16
"""

# Import required modules
import arcpy, os

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
arcpy.env.overwriteOutput = True

# Define local variable(s)
demGrid = "dem10"
demRemap = arcpy.sa.RemapRange([[294, 348, 0], [348, 374, 1], [374, 391, 2], [391, 408, 3], [408, 478, 4]])
outWorkspace = "D:/GitHub/GitHub-Rasters/scratch.gdb"

# Perform geoprocessing and trap errors
try:
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
        outReclass = arcpy.sa.Reclassify(demGrid, "VALUE", demRemap, "NODATA")
        outReclass.save(os.path.join(outWorkspace,  "dem10_rc1"))
        arcpy.CheckInExtension("Spatial")
    else:
        print("Required Spatial Analyst extension is not available!")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except:
    print("Warning - An unexpected error occurred...")

finally:
    print("Script ran to completion...excellent!")  