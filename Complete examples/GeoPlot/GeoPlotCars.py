import geoplotlib
from geoplotlib.colors import ColorMap
import json

# PROCESS DATA

# Assign color based on production

def get_color(properties):
    country = properties['NAME']
    production = get_production(country)
    if not(production is None):
        production = production.replace(' ', '')
        return cmap.to_color(float(production), get_max_production(), 'lin')
    else:
        return [0, 0, 0, 0]

# Find largest production in dataset

def get_max_production():
    allprod = []
    for data in cars:
        production = data.get('production')
        production = production.replace(' ', '')
        allprod.append(float(production))
    return max(allprod)

# Find production of a country

def get_production(country):
    for data in cars:
        if data.get('country') == country:
            return data.get('production')
    return None


data = open('cars.json')
cars = json.load(data)

# VISUALIZE DATA

cmap = ColorMap('RdYlGn', alpha=255, levels=100)
# Use GeoJSON of europe for borders
geoplotlib.geojson('europe.json', fill=True, color=get_color, f_tooltip=lambda properties: properties['NAME'])
geoplotlib.show()
