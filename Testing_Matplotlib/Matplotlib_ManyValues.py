import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

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

axs[0].plot(x,sin_x, linestyle='solid')
axs[0].plot(x,cos_x, linestyle='dashed')
axs[0].plot(x,sin_2x, linestyle='dashdot')
axs[0].plot(x,sqrt_x, linestyle='dotted')
axs[0].plot(x,cos_x_2, linestyle=(2, (3, 1, 5, 1)))

# Scatter plot

axs[1].scatter(x,sin_x, marker='8')
axs[1].scatter(x,cos_x, marker='1')
axs[1].scatter(x,sin_2x, marker='H')
axs[1].scatter(x,sqrt_x, marker='$?$')
axs[1].scatter(x,cos_x_2, marker='v', edgecolors=['black','white'])


# Bar plot

colors = ['lightgrey','dimgrey']
hatches = ['/','x','\\']
axs[2].bar(data['company'], data['profit'], color=colors)

hatch = 0
for patch in axs[2].patches:
    patch.set_hatch(hatches[hatch])
    if hatch < 2:
        hatch = hatch +1
    else:
        hatch = 0

for tick in axs[2].get_xticklabels():
    tick.set_rotation(30)
    tick.set_horizontalalignment('right')

plt.show()