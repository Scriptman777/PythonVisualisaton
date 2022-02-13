import numpy as np
import pygal
from pygal.style import Style, DarkGreenStyle

# Sample data

data = np.random.randint(low=0,high=50,size=6).tolist()
cats = ['F','E','D','C','B','A']

smooth_x = np.linspace(0,2*np.pi,500)
smooth_y = np.sin(smooth_x)

random_points = [(i, np.random.randint(50)) for i in range(50)]


# Experiments


style = Style(colors=('#ff0000', '#ff9100', '#ffff00', '#0008f5', '#006605', '#00ff0d'))

bar = pygal.Bar(style=style)
bar.title = 'Bar chart'
for grade in cats:
    bar.add(grade, data[cats.index(grade)])
bar.show_legend = False
bar.render_in_browser()

line = pygal.Line(style=DarkGreenStyle, fill=True)
line.title = 'Line chart'
line.x_labels = smooth_x
line.add('Value', smooth_y)
line.show_legend = False
line.render_in_browser()

scatter = pygal.XY(stroke=False)
scatter.title = 'Scatter chart'
scatter.add('XY', random_points, dots_size=4)
scatter.show_legend = False
scatter.render_in_browser()
