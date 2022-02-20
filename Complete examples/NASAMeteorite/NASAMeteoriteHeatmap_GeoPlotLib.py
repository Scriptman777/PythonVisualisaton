import csv
import geoplotlib
import pandas as pd
from geoplotlib.utils import DataAccessObject

lons = []
lats = []
names = []

# PROCESS DATA

with open("Meteorite_Landings.csv", encoding='utf-8') as landings:
    # Read CSV file
    reader = csv.DictReader(landings)
    for data in reader:
        # Get location and name
        if not data['GeoLocation'] == "(0.0, 0.0)" and data['GeoLocation'].strip():
            lons.append(float(data['reclong']))
            lats.append(float(data['reclat']))
            names.append(data['name'])

# Create pandas DataFrame of locations
static_dict = {'name':names ,'lon':lons, 'lat':lats,}
df = pd.DataFrame(static_dict)
# Convert to geoplotlib DataAccessObject
dao = DataAccessObject(df) 

# VISUALIZE DATA

geoplotlib.kde(dao,bw = [2,2])
geoplotlib.show()