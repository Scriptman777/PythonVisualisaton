import numpy as np
import pandas as pd


# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)


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

# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data_cats, orient='index')


# Other



print("TODO")