# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo13_3.py
    Author: Shawn Hutchinson
    Description:  Example script that performs map algebra on a raster object
    Date created: November 19, 2025
    Python Version: 3.11.11
"""

# Import required modules:
import arcpy, os

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
arcpy.env.overwriteOutput = True
arcpy.env.mask = "KonzaBoundary"
arcpy.env.extent = "KonzaBoundary"

# Define local variable(s)
demGrid = arcpy.Raster("dem10")
outWorkspace = "D:/GitHub/GitHub-Rasters/scratch.gdb"

# Perform geoprocessing and trap errors
try:
    outGrid = demGrid * 3.28984
    outGrid.save(os.path.join(outWorkspace, "elev_ft_kz3"))

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except:
    print("Warning - An unexpected error occurred...")    

finally:
    print("Script ran to completion...excellent!")
