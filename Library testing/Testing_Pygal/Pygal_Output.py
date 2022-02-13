import numpy as np
import pygal

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

fig1 = pygal.Bar()
fig1.title = 'Python list'
fig1.x_labels = cats
fig1.add('Grades', data)


# Export


fig1.render_to_file('export.svg')
fig1.render_in_browser()
fig1.render_to_png('export.png')