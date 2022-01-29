import numpy as np
import pandas as pd
import plotly.express as px

# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

fig = px.bar(x=cats, y=data, title="Python list")
fig.show()


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

fig2 = px.bar(x=tuple_cats, y=tuple_data, title="Python tuple")
fig2.show()


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

fig3 = px.bar(dict_data, x='cathegories', y='values', title="Python dictionary")
fig3.show()



# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

np_data = np.array(data)
np_cats = np.array(cats)

fig4 = px.bar(x=np_cats, y=np_data, title="Numpy array - cathegories")
fig4.show()

fig5 = px.line(x=x, y=y, title="Numpy Arrays - x,y")
fig5.show()


# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data)


fig6 = px.bar(df, x='cathegories', y='values', title="Pandas Dataframe")
fig6.show()