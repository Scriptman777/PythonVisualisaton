import numpy as np
import holoviews as hv
import webbrowser
from bokeh.palettes import Spectral6, cividis

# Sample data

dict_data = {
    "values": np.random.randint(low=0,high=50,size=6).tolist(),
    "categories": ['F','E','D','C','B','A']
    }

smooth_points = [(0.1*i, np.sin(0.1*i)) for i in range(500)]

random_points = [(i, np.random.randint(50)) for i in range(50)]


graphlist = []

# Experiments

hv.extension('bokeh')

bar_chart = hv.Bars(dict_data, "categories" , "values", label='Bar chart')
bar_chart.opts(width=1000, height=500, axiswise=True, xlabel='Kategorie', ylabel='Počet', color='categories', cmap='RdYlGn', show_legend=False)

graphlist.append(bar_chart)

curve_chart = hv.Curve(smooth_points, label='Line chart')
curve_chart.opts(width=1000, height=500, axiswise=True, line_width=3, color='red', line_dash='dashed')

graphlist.append(curve_chart)

scatter_chart = hv.Scatter(random_points, label='Scatter chart')
scatter_chart.opts(width=1000, height=500, axiswise=True, cmap='Turbo', color='y', size=10, marker='hex')

graphlist.append(scatter_chart)

layout = hv.Layout(graphlist).cols(1)

hv.save(layout, 'customisation.html')

webbrowser.open('customisation.html')