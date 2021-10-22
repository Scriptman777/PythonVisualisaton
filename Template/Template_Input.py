import numpy as np
import pandas as pd


# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']


# Python dictionary

dict_data = {
    "values": np.random.randint(low=0,high=50,size=6).tolist(),
    "cathegories": ['F','E','D','C','B','A']
    }


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)


# Numpy Array

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)


# Pandas Dataframe

df = pd.DataFrame(dict_data)


# Other



print("TODO")