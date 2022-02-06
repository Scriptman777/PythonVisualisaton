import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.io import show, curdoc, save, output_file
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap, factor_hatch

# Sample data

data = pd.read_csv('MOCK_DATA.csv')

x = np.linspace(0,2*np.pi,50)
sin_x = np.sin(x)
cos_x = np.cos(x)
sin_2x = np.sin(2*x)
cos_x_2 = np.cos(x)*2
sqrt_x = np.sqrt(x)

# Line plot

line = figure(height=350, title="Lines")
line.line(x=x, y=sin_x, line_width=3)
line.line(x=x, y=cos_x, line_width=3, line_color="orange")
line.line(x=x, y=sin_2x, line_width=3, line_color=(255,0,0), line_dash=(4, 4))
line.line(x=x, y=cos_x_2, line_width=3, line_color="green", line_dash="dotted")
line.line(x=x, y=sqrt_x, line_width=3, line_color="#a240a2")
line.circle(x, sqrt_x, color="purple")

# Scatter plot

scatter = figure(height=350, title="Scatter")
scatter.scatter(x=x, y=sin_x, marker="hex", size=10, fill_color="#ADD8E6")
scatter.scatter(x=x, y=cos_x, marker="hex_dot", size=10, fill_color="#ADD8E6")
scatter.scatter(x=x, y=sin_2x, marker="triangle_pin", size=10, fill_color="#ADD8E6")
scatter.scatter(x=x, y=cos_x_2, marker="circle_y", size=10, fill_color="#ADD8E6")
scatter.scatter(x=x, y=sqrt_x, marker="square_x", size=10, fill_color="#ADD8E6")



# Bar plot

df_source = ColumnDataSource(data)

bar = figure(height=350, title="Bar", x_range=data['company'])
bar.vbar(x="company", top="profit", source=df_source, width=0.9, legend_group='exchange',  hatch_pattern=factor_hatch('exchange', patterns=["right_diagonal_dash","blank"], factors=data['exchange'].unique()), fill_color=factor_cmap('arbitraryCategory', palette=Spectral5, factors=data['arbitraryCategory'].unique()))
bar.legend.orientation = "horizontal"
bar.legend.location = "top_center"
bar.xaxis.major_label_orientation = "vertical"
bar.xgrid.grid_line_color = None


graph = gridplot([line, scatter, bar], ncols=1)
output_file("ManyValues.html")
show(graph)