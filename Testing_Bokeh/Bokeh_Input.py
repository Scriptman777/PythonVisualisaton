import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.io import show, curdoc, save, output_file
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource







# Python list

cats = ['F','E','D','C','B','A']
data = np.random.randint(low=0,high=50,size=6).tolist()

fig1 = figure(x_range=cats, height=350, title="Python list")
fig1.vbar(x=cats, top=data, width=0.9)


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

fig2 = figure(x_range=tuple_cats, height=350, title="Python tuple")
fig2.vbar(x=tuple_cats, top=tuple_data, width=0.9)


# Python dictionary

dict_data = {
    "values": np.random.randint(low=0,high=50,size=6).tolist(),
    "cathegories": ['F','E','D','C','B','A']
    }

dict_data_cats = {
    "F": 3,
    "E": 10,
    "D": 30,
    "C": 25,
    "B": 15,
    "A": 10
    }




fig3 = figure(x_range=dict_data['cathegories'], height=350, title="Python dict")
fig3.vbar(x='cathegories', top='values', width=0.9, source=dict_data)

source = ColumnDataSource(data=dict_data)

fig4 = figure(x_range=dict_data['cathegories'], height=350, title="Python dict => Column source")
fig4.vbar(x="cathegories", top="values", source=source, width=0.9)


# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

np_data = np.array(data)
np_cats = np.array(cats)

fig5 = figure(height=350, title="NumPy array")
fig5.line(x=x, y=y)


# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data)

df_source = ColumnDataSource(df)

fig6 = figure(x_range=dict_data['cathegories'], height=350, title="Pandas DataFrame")
fig6.vbar(x="cathegories", top="values", source=df_source, width=0.9)



# Other


graph = gridplot([fig1, fig2, fig3, fig4, fig5, fig6], ncols=2)
output_file("Input.html")
show(graph)