import webbrowser
import pandas as pd
import holoviews as hv
import numpy as np

hv.extension('bokeh')

# Sample data

x = np.linspace(0,2*np.pi,50)
sin_x = np.sin(x)
cos_x = np.cos(x)
sin_2x = np.sin(2*x)
cos_x_2 = np.cos(x)*2
sqrt_x = np.sqrt(x)

data = pd.read_csv('MOCK_DATA.csv')

key_dimensions = [('company', 'Company name')]
value_dimensions = [('profit', 'Profit'), ('employees', 'Number of employees'), ('exchange', 'Exchange'), ('arbitraryCategory', 'Category with no meaning')]


# Layout
graphlist = []

# Line plot

line1 = hv.Curve((x, sin_x))
line1.opts(width=1200, height=500, line_width=3, color='red', line_dash='dashed')

line2 = hv.Curve((x, cos_x))
line2.opts(width=1200, height=500, line_width=3, color='green', line_dash='dotted')

line3 = hv.Curve((x, sin_2x))
line3.opts(width=1200, height=500, line_width=3, color='blue', line_dash='dotdash')

line4 = hv.Curve((x, cos_x_2))
line4.opts(width=1200, height=500, line_width=3, color='purple', line_dash='dashdot')

line5 = hv.Curve((x, sqrt_x))
line5.opts(width=1200, height=500, line_width=3, color='orange')


all_line = line1 * line2 * line3 * line4 * line5
all_line.relabel("Line chart")
graphlist.append(all_line)


# Scatter plot

scatter1 = hv.Scatter((x, sin_x))
scatter1.opts(width=1200, height=500, size=5, marker='hex')

scatter2 = hv.Scatter((x, cos_x))
scatter2.opts(width=1200, height=500, size=5, marker='cross')

scatter3 = hv.Scatter((x, sin_2x))
scatter3.opts(width=1200, height=500, size=5)

scatter4 = hv.Scatter((x, cos_x_2))
scatter4.opts(width=1200, height=500, size=5, marker='circle')

scatter5 = hv.Scatter((x, sqrt_x))
scatter5.opts(width=1200, height=500, size=5, marker='triangle')


all_scatter = scatter1 * scatter2 * scatter3 * scatter4 * scatter5
all_scatter.relabel("Scatter chart")
graphlist.append(all_scatter)


# Bar plot

bar_chart = hv.Bars(data, key_dimensions, value_dimensions, label='Bar chart')
bar_chart.opts(width=1200, height=500, color='exchange', cmap='Colorblind', xrotation=45) # Hatches are not supported

graphlist.append(bar_chart)


layout = hv.Layout(graphlist).cols(1)

hv.save(layout, 'ManyValues_Bokeh.html')

webbrowser.open('ManyValues_Bokeh.html')