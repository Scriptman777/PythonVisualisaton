import webbrowser
import pandas as pd
import holoviews as hv

hv.extension('plotly')

# Sample data

data = pd.read_csv('MOCK_DATA.csv')

key_dimensions = [('company', 'Company name')]
value_dimensions = [('profit', 'Profit'), ('employees', 'Number of employees'), ('exchange', 'Exchange'), ('arbitraryCategory', 'Category with no meaning')]

# Bar plot

bar_chart = hv.Bars(data, key_dimensions, value_dimensions, label='Bar chart with a large amount of data')
bar_chart.opts(width=1200, height=500) #color attribute results in an error. Bgcolor is the only available color-related attribute

hv.save(bar_chart, 'ManyValues_Plotly.html')

webbrowser.open('ManyValues_Plotly.html')

