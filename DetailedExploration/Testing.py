import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x1 = ['Pondělí','Úterý','Středa','Čtvrtek','Pátek','Sobota','Neděle']
y1 = [1,2,3,3.5,2,3,4]


fig, ax = plt.subplots(figsize =(11, 9))
fig.tight_layout(pad=3.0)


data = np.random.random(100)
data = np.append(data,1.5)
df = pd.DataFrame(data)
df.boxplot(ax=ax)
ax.set_title("Krabicový graf")
ax.grid(b=None)



plt.show()