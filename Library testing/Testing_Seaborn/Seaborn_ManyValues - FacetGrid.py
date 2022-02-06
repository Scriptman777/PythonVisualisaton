import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


sns.set()

# Sample data

data = pd.read_csv('MOCK_DATA.csv')


sns.catplot(data=data, col="arbitraryCategory", row="exchange", kind="bar")

plt.show()


