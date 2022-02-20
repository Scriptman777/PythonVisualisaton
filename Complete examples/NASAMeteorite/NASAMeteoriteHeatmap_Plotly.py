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

fig = px.density_mapbox(df, lat='lat', lon='lon', radius=5, center=dict(lat=0, lon=180), zoom=0, mapbox_style="stamen-terrain")
fig.write_html("Plotly output heatmap.html")