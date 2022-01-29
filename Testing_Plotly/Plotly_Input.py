import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go



fig = make_subplots(rows=3, cols=2, subplot_titles=("Python list", "Python tuples", "Python dictionary - lists", "Numpy array - x,y", "Numpy array - cathegories", "Pandas DataFrame"))




# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

fig.add_trace(
    go.Bar(x=cats, y=data),
    row=1, col=1
)


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

fig.add_trace(
    go.Bar(x=tuple_cats, y=tuple_data),
    row=1, col=2
)


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

fig.add_trace(
    go.Bar(x=dict_data['cathegories'], y=dict_data['values']),
    row=2, col=1
)

# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

np_data = np.array(data)
np_cats = np.array(cats)

fig.add_trace(
    go.Scatter(x=x, y=y),
    row=2, col=2
)

fig.add_trace(
    go.Bar(x=np_cats, y=np_data),
    row=3, col=1
)

# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data)

fig.add_trace(
    go.Bar(x=df['cathegories'],y=df['values']),
    row=3, col=2
)


fig.update_layout(showlegend=False)
fig.show()