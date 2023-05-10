# geoid_assignment
The script uses GeoPandas and the spatial join functionality to optimize the processing speed.

# Website used for shapefile https://www.census.gov/cgi-bin/geo/shapefiles/index.php
# ----------------------------------------------------------------------------
# Script Name: spatial_join_geoid_assignment.py
# Author: Redwan Ahmed Salman
# Created: 28-04-2023
# ----------------------------------------------------------------------------
# Purpose:
# This script reads a CSV file containing latitude and longitude coordinates
# and associates each point with its corresponding geographic identifier
# (GEOID under Census Blocks) based on the 2022 Census data. The script uses GeoPandas and the
# spatial join functionality to optimize the processing speed.
# ----------------------------------------------------------------------------
# Performance:
# The script is optimized to handle large datasets efficiently. For example,
# it can process 1 million rows of latitude and longitude coordinates in
# approximately 1 minute. This excludes the time taken to load the shapefile.
# ----------------------------------------------------------------------------
