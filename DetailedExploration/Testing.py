import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x1 = [1,2,3,4,5,6,7]
y1 = [1,2,3,3.5,2,3,4]


fig, ax = plt.subplots(3, figsize =(11, 9))
fig.tight_layout(pad=3.0)


ax[0].scatter(x1,y1, color="red")
ax[0].set_title("Bodový graf")
ax[1].plot(x1,y1, color="red")
ax[1].set_title("Spojnicový graf")
ax[2].plot(x1,y1, color="red")
ax[2].fill_between(x1, y1, color="red", alpha=0.2)
ax[2].set_title("Plošný graf")


plt.show()