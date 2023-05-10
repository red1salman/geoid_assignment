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

import geopandas as gpd
from shapely.geometry import Point
import os
import fiona
import time
import logging

os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)



# Read your CSV file
csv_file = 'state_AR.csv' ############################################################################################################################################################# Change based on state

#df = pd.read_csv(csv_file)
df = pd.read_csv(csv_file, dtype={'GEOID20': str})
# df = df.head(1000000)
print(df.head())
# exit()
start_time_shp = time.time()

# Read the shapefile
shapefile_path = "...tl_2022_AR_05_tabblock20/tl_2022_05_tabblock20.shp" ################# Change based on state

with fiona.Env(SHAPE_RESTORE_SHX='YES'):
    gdf = gpd.read_file(shapefile_path)

elapsed_time_shp = time.time() - start_time_shp
print(f"Elapsed time for reading shapefile: {elapsed_time_shp:.2f} seconds")

start_time = time.time()

# Convert DataFrame to GeoDataFrame
geometry = [Point(xy) for xy in zip(df['LON'], df['LAT'])]
gdf_points = gpd.GeoDataFrame(df, crs=gdf.crs, geometry=geometry)

# Perform spatial join
gdf_joined = gpd.sjoin(gdf_points, gdf, how='left', predicate='within')

# Rename and drop unnecessary columns
gdf_joined = gdf_joined.rename(columns={'GEOID20': 'GEOID'})
gdf_joined = gdf_joined.drop(columns=['index_right', 'geometry'])
gdf_joined = gdf_joined[['ROW_WID', 'LAT', 'LON', 'STATE', 'GEOID']]  # Keep only the desired columns


# Save the DataFrame with the new column to a new CSV file
# The csv will not have leading zeros
gdf_joined.to_csv('AR_geoid.csv', index=False) ############################################################################################################################### Change based on state


# Check the total number of rows in the GeoDataFrame
total_rows = len(gdf_joined)
print(f"Total number of rows joined: {total_rows}")
print()
print(gdf_joined.head())
print()
elapsed_time_seconds = time.time() - start_time  # Calculate the elapsed time in seconds
elapsed_time_hours = elapsed_time_seconds / 3600

hours, remainder = divmod(elapsed_time_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Elapsed time for conversion: {elapsed_time_hours:.2f} hours")
print(f"Elapsed time for conversion: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
print(elapsed_time_seconds)
