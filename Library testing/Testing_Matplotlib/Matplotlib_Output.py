import numpy as np
import matplotlib.pyplot as plt


# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

# Create graph

fig, axs = plt.subplots(figsize=(10, 5))
axs.bar(cats,data)

# Export

print(plt.gcf().canvas.get_supported_filetypes())

plt.savefig('plot.png')
plt.savefig('plot.jpeg', format='jpeg')
plt.savefig('plot.pdf', format='pdf')
plt.savefig('plot.svg', format='svg')
plt.savefig('plot.raw', format='raw')
plt.savefig('plot.tiff', format='tiff')