# GitHub-RasterClasses
Exercise for GEOG 728 Programming for Geographic Analysis at Kansas State University

### Instructions:

Accept the GitHub Classroom assignment <code>GitHub-RasterClasses</code> and clone the new repository as a local personal repository.  We will use the same compressed ArcGIS Pro project file from the <code>GitHub-Rasters</code> exercise for this week's work.  Recall that the compressed project file is too large to store in GitHub.  Instead, you can download it from last week's Canvas module or <code>W:\GEOG\Courses\GEOG728\Exercises</code>,  Uncompress the provided ZIP file to access the ArcGIS Pro project file in your local repository workspace.  The only file which needs to be pushed to origin at the conclusion of the exercise is a single Python script.  There is no requirement to prepare and submit a script-based tool.  Should you encounter difficulties during the week, seek assistance by posting an issue in GitHub.

### Task:

Edit the provided Python file called <code>GitHub-RasterClasses.py</code> to include your coding work from last week.  Remember that you were to create a new stand-alone script that calculates normalized difference vegetation index (NDVI) from a multi-band raster dataset.  Your script was to have included the following features and capabilities:

1. Uses one of the three available Landsat 8 images as the raster input.
2. Uses at least one, but no more than three, local variables.
3. Uses only Spatial Analyst functions – no Python math!
4. Checks out/in the Spatial Analyst extension.
5. Uses at least one "if-else" and "try-except" block for error trapping.
6. Saves one file – the output NDVI grid - to a workspace other than current workspace using one or more os module functions.
7. Prints only one message – either script success, user lacks the required extension, or a Level 2 geoprocessing error message.
8. The "script success" message should also report name of output file, its spatial resolution, and units.

Build on this script to include the following NEW features and capabilities:

1. Uses a Spatial Analyst Remap class to reclassify your calculated NDVI output into the following 6 classes:
   * 0 = -1 – 0
   * 1 = 0 – 0.2
   * 2 = 0.2 – 0.4
   * 3 = 0.4 – 0.6
   * 4 = 0.6 – 0.8
   * 5 = 0.8 – 1
2. Uses new environment classes and setting to ensure your final result:
   * Has the same spatial extent of Fort Riley
   * Contains valid NDVI values only for cells within the boundary of Fort Riley
3. Saves two files – the original output NDVI grid and the reclassified NDVI grid - to a workspace other than current workspace using one or more os module functions.

## Rubric:

Review the assignment rubric available on Canvas for additional details on how your work will be assessed. Double-check that your script includes a complete header section, uses good commenting, incorporates line spaces between blocks of code, and reads input and writes output to current workspace.

## Submission:

Commit your code changes for <code>GitHub-RasterClasses.py</code> to your assignment repository on GitHub.
