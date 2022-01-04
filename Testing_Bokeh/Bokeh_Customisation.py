import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, curdoc, save, output_file
from bokeh.layouts import gridplot
from bokeh.palettes import Spectral6, cividis
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

smooth_x = np.linspace(0,2*np.pi,500)
smooth_y = np.sin(smooth_x)

random_x = np.linspace(0,100,50)
random_y = np.random.randint(50, size=50)

# Experiments


bar_source = ColumnDataSource(data=dict(data=data, cats=cats, color=Spectral6))

fig1 = figure(x_range=cats, height=350, title="Bar", x_axis_label='Kategorie', y_axis_label='Počet')
fig1.vbar(x="cats", top="data", width=0.9, color='color', source=bar_source)


fig2 = figure(height=350, title="Line")
fig2.line(x=smooth_x, y=smooth_y, line_width=3, line_color=(255, 0, 0), line_dash="dashed")


colors = cividis(50)
fig3 = figure(height=350, title="Scatter")
fig3.scatter(x=random_x, y=random_y, marker="hex", size=10, fill_color=colors)


graph = gridplot([fig1, fig2, fig3], ncols=1)
output_file("Customisation.html")
show(graph)