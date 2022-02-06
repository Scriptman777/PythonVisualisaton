import numpy as np

from bokeh.plotting import figure
from bokeh.io import show, save, output_file, export_svg
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource


# Sample data

cats = ['F','E','D','C','B','A']
data = np.random.randint(low=0,high=50,size=6).tolist()

fig1 = figure(x_range=cats, height=350, title="Python list")
fig1.vbar(x=cats, top=data, width=0.9)


# Export

save(fig1, "Output.html")
# export_png(fig1)
