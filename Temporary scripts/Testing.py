import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x1 = ['Pondělí','Úterý','Středa','Čtvrtek','Pátek','Sobota','Neděle']
y1 = [1,2,3,3.5,2,3,4]


fig, ax = plt.subplots(2, figsize =(8, 10))
fig.tight_layout(pad=3.0)


n = 10000
x = np.random.standard_normal(n)
y = x + np.random.standard_normal(n)

ax[0].hexbin(x, y, gridsize=70, cmap='gist_rainbow')

ax[1].hexbin(x, y, gridsize=70, cmap='inferno')

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))



plt.show()