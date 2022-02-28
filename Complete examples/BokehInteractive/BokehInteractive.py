import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import figure

# GET DATA

# Create x axis
positions = np.linspace(-0.9,0.9,100)
# Compute default values for the function
values = []
x = 0.5
r = 3
for pos in range(100):
    values.append(x-1)
    x = r*x*(1-x)

source = ColumnDataSource(data=dict(x=positions, y=values))

# VISUALIZE DATA

plot = figure(title="Logistical map", width=1200, height=700)
plot.line('x', 'y', source=source, line_width=3)

# Create sliders for user interaction
r_value = Slider(title="Value of R", value=3, start=2.4, end=3.99, step=0.01)
x_value = Slider(title="Value of X", value=0.5, start=0, end=1, step=0.01)

# Function to update data
def update_values(attrname, old, new):
    positions = np.linspace(-0.9,0.9,100)
    values = []

    r = r_value.value
    x = x_value.value

    for pos in range(100):
        values.append(x-1)
        x = r*x*(1-x)
    source.data = dict(x=positions, y=values)

# Handlers to update when values are changed
r_value.on_change('value',update_values)
x_value.on_change('value',update_values)

curdoc().theme = 'dark_minimal'
curdoc().add_root(row(column(r_value,x_value), plot))

# Needs to be started as a server
# bokeh serve --show E:\Users\Dokumenty\FIM\BC\BCWork\BokehInteractive\BokehInteractive.py