import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create figure

fig, axs = plt.subplots(4, 2, figsize=(10, 8))
fig.tight_layout(pad=3.0)



# Python list

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

axs[0][0].bar(cats,data)
axs[0][0].set_title("Python list")


# Python tuple

tuple_data = tuple(data)
tuple_cats = tuple(cats)

axs[0][1].bar(tuple_cats,tuple_data)
axs[0][1].set_title("Python tuples")

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

# Cannot input dictionaries directly

axs[1][0].bar(dict_data['cathegories'],dict_data['values'])
axs[1][0].set_title("Python dictionary - lists")
axs[1][1].bar(dict_data_cats.keys(),dict_data_cats.values())
axs[1][1].set_title("Python dictionary - values")


# Numpy Arrays

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)

np_data = np.array(data)
np_cats = np.array(cats)

axs[2][0].plot(x,y)
axs[2][0].set_title("Numpy array - x,y")
axs[2][1].bar(np_cats,np_data)
axs[2][1].set_title("Numpy array - cathegories")

# Pandas Dataframe

df = pd.DataFrame.from_dict(dict_data_cats, orient='index')

axs[3][0].plot(df)
axs[3][0].set_title("Pandas dataframe")

# axs[3][1].bar(df) - not possible

# can still be plotted with:
df.plot(kind='bar', ax=axs[3][1])
axs[3][1].set_title("Pandas dataframe .plot()")

# Show output

plt.show()