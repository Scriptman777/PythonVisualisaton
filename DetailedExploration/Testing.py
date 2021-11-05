import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x1 = [1,2,3,4,5,6,7]
y1 = [1,1,1,1,2,3,4]

x2 = [1,5,6,7]
y2 = [1,2,3,4]



fig, ax = plt.subplots(2, figsize =(11, 9))
ax[1].plot(x1,y1, color="green")
ax[1].plot(x2,y2, color="red")

ax[0].scatter(x2,y2, color="red")



plt.show()