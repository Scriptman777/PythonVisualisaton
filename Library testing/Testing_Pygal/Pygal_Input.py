import numpy as np
import pandas as pd
import pygal


# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

fig1 = pygal.Bar()
fig1.title = 'Python list'
fig1.x_labels = cats
fig1.add('Grades', data)
fig1.render_to_file('fig1.svg')


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

fig2 = pygal.Bar()
fig2.title = 'Python tuple'
fig2.x_labels = tuple_cats
fig2.add('Grades', tuple_data)
fig2.render_to_file('fig2.svg')


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



# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

np_data = np.array(data)
np_cats = np.array(cats)

fig3 = pygal.Bar()
fig3.title = 'NumPy array - bar'
fig3.x_labels = np_cats
fig3.add('Grades', np_data)
fig3.render_to_file('fig3.svg')

fig4 = pygal.Line()
fig4.title = 'NumPy array - line'
fig4.x_labels = x
fig4.add('Value', y)
fig4.render_to_file('fig4.svg')

# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data)


# Other
