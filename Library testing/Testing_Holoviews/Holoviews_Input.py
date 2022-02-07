import numpy as np
import pandas as pd
import holoviews as hv
import webbrowser

hv.extension('bokeh')
graphlist = []

# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

# graphlist.append(hv.Bars(cats, data)) - List is not usable for Bar graphs


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

tuples_for_hv = []

# Tuples have to be in a list of (name,data) format

for x in range(0,len(tuple_cats)):
    new_tuple = (tuple_cats[x],tuple_data[x])
    tuples_for_hv.append(new_tuple)

graphlist.append(hv.Bars(tuples_for_hv, label='Tuple list'))

# Python dictionary

dict_data = {
    "values": np.random.randint(low=0,high=50,size=6).tolist(),
    "categories": ['F','E','D','C','B','A']
    }

dict_data_cats = {
    "F": 3,
    "E": 10,
    "D": 30,
    "C": 25,
    "B": 15,
    "A": 10
    }

graphlist.append(hv.Bars(dict_data, "categories" , "values", label='Dictionary - key dimensions'))

graphlist.append(hv.Bars(dict_data_cats, hv.Dimension('Final mark'), 'Count', label='Dictionary - value dimensions')) # Holoviews can work with dictionary with many dimensions

# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

curve = hv.Curve((x, y), label='NumPy array').opts(axiswise=True)

graphlist.append(curve)

# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data)

graphlist.append(hv.Bars(df, "categories", "values", label='pandas DataFrame'))


# Other


layout = hv.Layout(graphlist).cols(2)

hv.save(layout, 'plot.html', backend='bokeh')

webbrowser.open('plot.html')