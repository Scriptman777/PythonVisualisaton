import csv
import geoplotlib
import pandas as pd
from geoplotlib.utils import DataAccessObject

lons = []
lats = []
names = []

with open("Meteorite_Landings.csv", encoding='utf-8') as landings:
    reader = csv.DictReader(landings)
    for data in reader:
        if not data['GeoLocation'] == "(0.0, 0.0)" and data['GeoLocation'].strip():
            lons.append(float(data['reclong']))
            lats.append(float(data['reclat']))
            names.append(data['name'])

static_dict = {'name':names ,'lon':lons, 'lat':lats,}
df = pd.DataFrame(static_dict)
dao = DataAccessObject(df) 


geoplotlib.kde(dao,bw = [2,2])
geoplotlib.show()