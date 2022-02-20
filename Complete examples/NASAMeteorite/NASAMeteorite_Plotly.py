import csv
import pandas as pd
import plotly.express as px

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

# VISUALIZE DATA

fig = px.scatter_geo(df, lat='lat', lon='lon', text='name')
fig.write_html("Plotly output.html")