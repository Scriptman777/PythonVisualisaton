import geoplotlib
from geoplotlib.colors import ColorMap
import json
import msvcrt

def get_color(properties):
    country = properties['NAME']
    production = get_production(country)
    if not(production is None):
        production = production.replace(' ', '')
        return cmap.to_color(float(production), 4661328, 'lin')
    else:
        return [0, 0, 0, 0]

def get_production(country):
    for data in cars:
        if data.get('country') == country:
            return data.get('production')
    return None

with open('cars.json') as data:
    cars = json.load(data)

cmap = ColorMap('RdYlGn', alpha=255, levels=100)
geoplotlib.geojson('europe.json', fill=True, color=get_color, f_tooltip=lambda properties: properties['NAME'])
geoplotlib.show()
