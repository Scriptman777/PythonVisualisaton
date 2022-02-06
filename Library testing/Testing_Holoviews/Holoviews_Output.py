import numpy as np
import holoviews as hv


# Sample data

dict_data = {
    "values": np.random.randint(low=0,high=50,size=6).tolist(),
    "categories": ['F','E','D','C','B','A']
    }

plot = hv.Bars(dict_data, "categories" , "values", label='Export test')

# Export


# Backends
hv.save(plot, 'export_bokeh.html', backend='bokeh')
hv.save(plot, 'export_matplotlib.png', backend='matplotlib')
hv.save(plot, 'export_plotly.html', backend='plotly')


# Formats
hv.save(plot, 'export.png', fmt='png', backend='matplotlib')
hv.save(plot, 'export.svg', fmt='svg', backend='matplotlib')
hv.save(plot, 'export.pdf', fmt='pdf', backend='matplotlib')
