import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

smooth_x = np.linspace(0,2*np.pi,500)
smooth_y = np.sin(smooth_x)

random_x = np.linspace(0,100,50)
random_y = np.random.randint(50, size=50)

# Experiments

fig, axs = plt.subplots(3, 1, figsize=(10, 8))
# Set space between graphs
fig.tight_layout(pad=3.0)


sns.barplot(x=cats, y=data, ax=axs[0], palette="flare")



sns.lineplot(x=smooth_x, y=smooth_y, ax=axs[1], color="red", linewidth=3)
# Annotation and other elements from Matplotlib work the same
axs[1].annotate('Maximum',xy=(1.575, 1), xytext=(1.575,0.5), arrowprops=dict(facecolor='red', shrink=0.05), horizontalalignment='center')


sns.scatterplot(x=random_x,y=random_y, ax=axs[2], palette="viridis", hue=random_x, legend=False)



plt.show()