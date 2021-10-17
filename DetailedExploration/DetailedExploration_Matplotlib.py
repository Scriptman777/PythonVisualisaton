import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("KIKM_PGRF2.csv", sep=';')
single_row = data.loc[data["Období/Hodn."] == "LS 2018/19"]
single_row = single_row.drop(['Období/Hodn.','4','3','2','1'],1)

columns = ['Bez hodnocení','Nevyhovující','Dostatečně','Uspokojivě','Dobře','Velmi dobře','Výborně']
values = single_row.values.tolist()[0]

colors = ['grey','red','yellow','cyan','blue','green','lime']

fig, ax = plt.subplots(figsize =(11, 9))
ax.bar(columns, values, width=0.8, color=colors)
ax.set_title('Výsledky studentů předmětu PGRF2 v letním semestru 2018/19')
ax.set_ylabel('Počet studentů')
ax.set_xlabel('Hodnocení')
ax.annotate('Všichni studenti\nu zkoušky uspěli',xy=(1, 1), xytext=(1,3), arrowprops=dict(facecolor='red', shrink=0.05), horizontalalignment='center')
for tick in ax.get_xticklabels():
    tick.set_rotation(30)


plt.show()