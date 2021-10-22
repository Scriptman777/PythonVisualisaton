import numpy as np


# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

smooth_x = np.linspace(0,2*np.pi,500)
smooth_y = np.sin(smooth_x)

random_x = np.linspace(0,100,50)
random_y = np.random.randint(50)

# Experiments

print("TODO")