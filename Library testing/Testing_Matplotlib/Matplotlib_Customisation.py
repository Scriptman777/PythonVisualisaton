import numpy as np
import matplotlib.pyplot as plt

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

smooth_x = np.linspace(0,2*np.pi,50)
smooth_y = np.sin(smooth_x)

random_x = np.linspace(0,100,50)
random_y = np.random.randint(50, size=50)

# Experiments

fig, axs = plt.subplots(3, 1, figsize=(10, 8))
# Set space between graphs
fig.tight_layout(pad=3.0)

# Bar chart

# Recolor bars, display error 
colors = ['red','yellow','cyan','blue','green','lime']
axs[0].bar(cats,data, color=colors, yerr=2)
# Rename cathegories
columns = ['Nevyhovující','Dostatečně','Uspokojivě','Dobře','Velmi dobře','Výborně']
axs[0].set_xticklabels(columns)
# Set label for axis
axs[0].set_ylabel('Počet studentů')
# Rotate tick labels
for tick in axs[0].get_xticklabels():
    tick.set_rotation(30)


# Line plot

axs[1].plot(smooth_x, smooth_y, linewidth=2, marker='+', markeredgecolor='red', color='black')
# Show grid
axs[1].grid()
# Annotate a part of the graph
axs[1].annotate('Maximum',xy=(1.575, 1), xytext=(1.575,0.5), arrowprops=dict(facecolor='red', shrink=0.05), horizontalalignment='center')


# Scatter plot

# Get colormap
colormap = plt.cm.get_cmap('magma')

axs[2].scatter(random_x, random_y, cmap=colormap, c=random_y, s=random_y/2, marker='D')


plt.show()