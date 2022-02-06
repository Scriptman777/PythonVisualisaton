import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


sns.set()

# Sample data

data = pd.read_csv('MOCK_DATA.csv')

x = np.linspace(0,2*np.pi,50)
sin_x = np.sin(x)
cos_x = np.cos(x)
sin_2x = np.sin(2*x)
cos_x_2 = np.cos(x)*2
sqrt_x = np.sqrt(x)


# Figure

fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Line plot

sns.lineplot(x=x, y=sin_x, ax=axs[0])
sns.lineplot(x=x, y=cos_x, ax=axs[0])
sns.lineplot(x=x, y=sin_2x, ax=axs[0])
sns.lineplot(x=x, y=cos_x_2, ax=axs[0])
sns.lineplot(x=x, y=sqrt_x, ax=axs[0])

# Scatter plot

sns.scatterplot(x=x, y=sin_x, ax=axs[1])
sns.scatterplot(x=x, y=cos_x, ax=axs[1], marker=">")
sns.scatterplot(x=x, y=sin_2x, ax=axs[1], marker="8")
sns.scatterplot(x=x, y=cos_x_2, ax=axs[1], marker="X")
sns.scatterplot(x=x, y=sqrt_x, ax=axs[1], marker="D")

# Bar plot


sns.barplot(data=data, x="company", y="profit", hue="arbitraryCategory", ax=axs[2], palette="hot_r", dodge=False)
axs[2].legend(bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=0.)

for tick in axs[2].get_xticklabels():
    tick.set_rotation(30)
    tick.set_horizontalalignment('right')

plt.show()


