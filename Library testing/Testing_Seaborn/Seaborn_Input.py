import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Create figure

fig, axs = plt.subplots(4, 2, figsize=(10, 8))
fig.tight_layout(pad=3.0)

# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

sns.barplot(x=cats, y=data, ax=axs[0][0])
axs[0][0].set_title("Python list")


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

#sns.barplot(x=tuple_cats, y=tuple_data, ax=axs[0][1])
# Tuples would have to be converted to lists with list()
axs[0][1].set_title("Python tuple")

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

# Dictionaries can be supplied in "data" parameter, x and y are keys
sns.barplot(data=dict_data, x="cathegories", y="values", ax=axs[1][0])
axs[1][0].set_title("Python dictionary - lists")
# In case of keys and values, conversion to lists is needed
sns.barplot(x=list(dict_data_cats.keys()), y=list(dict_data_cats.values()), ax=axs[1][1])
axs[1][1].set_title("Python dictionary - values")


# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

np_data = np.array(data)
np_cats = np.array(cats)

sns.lineplot(x=x,y=y, ax=axs[2][0])
axs[2][0].set_title("Numpy array - x,y")

sns.barplot(x=np_cats, y=np_data, ax=axs[2][1])
axs[2][1].set_title("Numpy array - cathegories")


# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data)

sns.barplot(data=df, x="cathegories", y="values", ax=axs[3][0])
axs[3][0].set_title("Pandas DataFrame")

# Other

plt.show()