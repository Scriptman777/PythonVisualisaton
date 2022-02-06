import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

fig, axs = plt.subplots(figsize=(10, 5))
sns.barplot(x=cats, y=data)

# Export

plt.savefig('plot.png')
plt.savefig('plot.jpeg', format='jpeg')
plt.savefig('plot.pdf', format='pdf')
plt.savefig('plot.svg', format='svg')
plt.savefig('plot.raw', format='raw')
plt.savefig('plot.tiff', format='tiff')