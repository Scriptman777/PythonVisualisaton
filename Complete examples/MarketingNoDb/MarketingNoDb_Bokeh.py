from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.palettes import Cividis
import numpy as np
from collections import Counter

female_ages = [44, 36, 40, 40, 44, 47, 28, 44, 43, 43, 49, 50, 48, 32, 38, 51, 27, 28, 35, 40, 38, 51, 36, 37, 37, 48, 43, 56, 31, 39, 34, 42, 45, 41, 36, 35, 34, 53, 50, 36, 31, 41, 45, 37, 48, 34, 26, 32, 38, 57, 52, 39, 39, 33, 44, 38, 37, 33, 31, 26, 45, 27, 37, 26, 39, 46, 24, 31, 50, 49, 39, 41, 39, 35, 43, 45, 45, 42, 41, 36, 36, 44, 31, 47, 49, 26, 55, 51, 48, 35, 38, 26, 51, 53, 34, 41, 52, 43, 27, 33, 40, 39, 28, 29, 35, 45, 35, 46, 42, 36, 38, 31, 48, 40, 47, 41, 43, 31, 31, 47, 32, 50, 46, 46, 29, 49, 41, 35, 32, 44, 38, 39, 52, 38, 37, 39, 36, 29, 40, 38, 24, 51, 56, 33, 48, 39, 54, 54, 43, 42, 41, 54, 47, 39, 60, 26, 44, 47, 29, 37, 36, 50, 36, 37, 42, 24, 39, 37, 49, 30, 38, 58, 41, 29, 40, 39, 47, 39, 45, 35, 42, 47, 31, 41, 38, 39, 33, 39, 40, 44, 34, 37, 41, 53, 27, 42, 36, 53, 36, 31, 33, 42, 45, 52, 38, 41, 45, 37, 52, 37, 40, 35, 45, 44, 28, 46, 45, 41, 44, 46, 39, 54, 40, 44, 41, 47, 44, 41, 40, 44, 53, 47, 46, 47, 33, 50, 37, 41, 40, 29, 41, 46, 42, 48, 49, 21, 38, 54, 46, 25, 39, 28, 29, 43, 52, 43, 29, 46, 39, 32, 48, 41, 46, 30, 43, 34, 36, 40, 51, 38, 53, 45, 41, 32, 47, 42, 45, 46, 40, 47, 50, 37, 25, 39, 39, 48, 41, 43, 30, 24, 34, 29, 39, 44, 48, 31, 47, 44, 33, 31, 34, 57, 55, 32, 44, 51, 45, 40, 43, 45, 34, 40, 28, 33, 43, 33, 34, 30, 45, 39, 37, 44, 30, 51, 33, 45, 47, 43, 25, 34, 31, 42, 33, 51, 41, 35, 44, 34, 38, 49, 55, 32, 46, 50, 41, 33, 32, 48, 37, 41, 24, 57, 49, 38, 51, 42, 46, 29, 24, 37, 39, 50, 26, 44, 39, 51, 47, 29, 44, 45, 43, 41, 30, 40, 35, 45, 55, 45, 35, 36, 37, 44, 53, 45, 38, 44, 46, 25, 51, 44, 40, 43, 51, 38, 46, 39, 45, 39, 26, 31, 53, 39, 46, 51, 53, 33, 32, 36, 41, 46, 52, 39, 46, 43, 32, 45, 40, 38, 41, 46, 55, 42, 37, 39, 37, 31, 65, 40, 54, 50, 38, 31, 34, 48, 35, 36, 32, 29, 48, 43, 46, 36, 43, 38, 35, 50, 30, 42, 41, 34, 58, 36, 35, 32, 53, 39, 47, 22, 36, 49, 44, 51, 36, 31, 44, 45, 39, 47, 39, 28, 42, 41, 55, 44, 48, 60, 45, 45, 50, 31, 39, 35, 35, 44, 36, 45, 40, 36, 38, 28, 45, 32, 28, 44, 35, 45, 31, 34, 30, 48, 56, 43, 42, 54, 44, 53, 41, 43, 42, 37, 44, 26, 34, 57, 34, 39, 51, 49, 41, 40, 39, 43, 34, 41, 38, 37, 39]
female_ages_hist, edges_f = np.histogram(female_ages, bins = 10)

male_ages = [47, 45, 50, 40, 32, 39, 45, 44, 42, 28, 34, 46, 47, 38, 43, 50, 28, 41, 39, 56, 43, 42, 41, 36, 49, 19, 31, 32, 44, 48, 33, 44, 39, 48, 35, 39, 34, 53, 30, 40, 53, 50, 49, 43, 44, 52, 50, 45, 48, 33, 45, 32, 38, 38, 34, 44, 40, 48, 37, 42, 44, 24, 35, 43, 47, 56, 43, 49, 43, 28, 32, 41, 34, 45, 43, 37, 40, 38, 39, 51, 40, 34, 29, 34, 40, 28, 39, 44, 37, 42, 55, 56, 25, 56, 45, 42, 50, 39, 43, 38, 29, 35, 49, 39, 44, 34, 37, 37, 49, 33, 35, 39, 40, 46, 40, 57, 43, 52, 45, 55, 41, 31, 37, 39, 40, 48, 34, 37, 33, 32, 38, 29, 41, 36, 37, 30, 48, 37, 37, 36, 52, 42, 32, 45, 37, 28, 44, 32, 45, 49, 49, 43, 39, 43, 41, 30, 34, 34, 37, 48, 23, 48, 48, 45, 36, 30, 51, 58, 31, 47, 32, 48, 26, 39, 52, 42, 52, 35, 29, 35, 40, 33, 36, 34, 33, 46, 22, 36, 34, 32, 36, 38, 29, 40, 45, 37, 47, 33, 40, 43, 28, 33, 48, 26, 51, 23, 32, 41, 39, 47, 32, 42, 35, 39, 34, 34, 38, 43, 56, 37, 20, 32, 49, 44, 33, 47, 31, 40, 46, 29, 27, 41, 30, 41, 35, 36, 45, 41, 45, 34, 36, 21, 40, 43, 42, 29, 40, 40, 41, 38, 34, 41, 41, 32, 46, 45, 49, 28, 35, 37, 50, 29, 43, 50, 37, 29, 50, 52, 36, 33, 36, 39, 40, 47, 42, 25, 35, 37, 23, 37, 43, 39, 32, 48, 46, 39, 32, 32, 50, 30, 53, 20, 36, 37, 40, 37, 30, 49, 44, 44, 36, 40, 26, 38, 41, 29, 38, 43, 23, 39, 39, 28, 37, 39, 40, 41, 34, 22, 33, 23, 42, 32, 34, 45, 45, 46, 43, 45, 46, 29, 48, 29, 34, 44, 49, 47, 22, 40, 30, 33, 38, 47, 39, 35, 31, 30, 44, 28, 41, 36, 35, 54, 46, 32, 24, 28, 43, 38, 36, 39, 38, 42, 35, 42, 37, 13, 46, 32, 33, 46, 28, 22, 44, 55, 33, 33, 36, 39, 37, 46, 54, 40, 36, 29, 45, 45, 36, 52, 52, 29, 41, 53, 49, 40, 50, 41, 38, 33, 41, 39, 39, 35, 39, 47, 42, 38, 39, 58, 38, 45, 51, 41, 28, 43, 19, 47, 65, 32, 45, 35, 34, 44, 42, 34, 35, 35, 49, 41, 41, 46, 39, 27, 54, 42, 45, 28, 26, 49, 45, 54, 47, 40, 42, 35, 35, 39, 44, 48, 44, 54, 32, 40, 47, 47, 46, 46, 54, 36, 43, 24, 36, 38, 52, 36, 46, 36, 41, 36, 34, 49, 36, 40, 37]
male_ages_hist, edges_m = np.histogram(male_ages, bins = 10)

result = ['2XL', '3XL', 'M', 'XS', 'S', '2XL', 'L', '2XL', '2XL', '2XL', 'S', '3XL', 'XS', 'L', 'L', '3XL', 'L', 'XL', 'XL', '3XL', 'XS', '2XL', 'XS', 'M', '2XL', 'XS', 'XS', '3XL', 'XS', 'L', '3XL', '3XL', 'S', 'L', 'XL', 'XL', 'S', '3XL', 'L', 'XS', 'XS', 'XS', 'XL', 'XS', 'L', '2XL', 'S', '3XL', 'L', 'S', 'S', 'XS', 'XS', 'XL', 'XL', '3XL', '2XL', '2XL', 'XL', 'XS', 'L', 'S', 'M', 'L', 'L', 'XL', '3XL', '2XL', '3XL', 'M', 'S', 'XS', '3XL', 'M', '2XL', '3XL', '3XL', '2XL', '3XL', 'L', '3XL', '2XL', 'L', 'XL', 'L', 'XS', 'XL', 'L', 'XS', 'L', 'XL', '2XL', '3XL', '2XL', 'L', 'L', 'M', 'L', '3XL', '2XL', 'S', '3XL', 'M', 'XL', 'S', 'S', 'XS', '3XL', 'S', '2XL', 'S', '3XL', 'S', 'S', '3XL', 'XL', 'M', 'XL', 'XS', 'XS', 'XL', 'M', 'S', '2XL', 'M', '2XL', 'L', '2XL', 'M', 'L', 'M', '2XL', 'M', 'L', '2XL', '3XL', 'XS', '3XL', 'XL', 'L', 'XS', '3XL', '2XL', 'L', 'M', 'XS', '2XL', 'S', 'XL', 'M', 'XL', 'S', '2XL', '2XL', 'M', 'M', '2XL', '2XL', 'XL', '2XL', '2XL', 'S', 'XS', '2XL', 'XS', 'XL', '2XL', 'XL', 'M', 'M', 'S', 'M', 'M', 'M', 'M', 'S', '2XL', 'M', 'L', 'XL', '3XL', 'S', 'M', 'XL', '2XL', 'S', 'S', '2XL', 'M', 'XS', 'XS', 'XS', 'XL', 'S', 'L', 'M', 'L', 'L', 'M', 'XS', '2XL', 'XS', 'S', '2XL', 'S', 'L', 'M', 'S', 'XS', '3XL', 'XL', 'S', 'L', '3XL', '2XL', 'XS', 'XL', 'XS', '3XL', 'XS', 'S', '2XL', 'L', 'S', 'M', '3XL', 'S', 'XS', '2XL', 'M', 'XL', 'S', '3XL', '3XL', 'XL', 'XS', 'L', '2XL', 'XL', 'XL', '2XL', '3XL', '3XL', '2XL', 'XS', '3XL', 'S', 'M', 'M', '2XL', 'M', 'XS', 'L', '2XL', 'XS', 'XS', '3XL', 'L', '2XL', 'XL', '2XL', '3XL', 'S', '3XL', 'M', 'M', 'XS', 'XS', '3XL', '2XL', 'XS', 'M', 'S', 'M', '3XL', '2XL', 'XL', 'M', 'XS', 'XL', 'M', '2XL', 'XL', '2XL', '3XL', 'XS', 'XS', 'L', '3XL', 'L', 'XS', 'M', 'XL', 'S', 'L', 'XS', 'S', 'XL', 'L', '2XL', '3XL', 'XS', 'S', 'XL', '3XL', 'XS', 'M', 'M', 'XL', 'M', 'S', 'S', '3XL', 'XS', 'S', 'XS', '2XL', 'XS', 'XS', 'XL', '3XL', 'XL', 'S', '2XL', '2XL', 'XL', 'L', 'XL', 'L', 'XS', 'XL', '2XL', '2XL', 'XS', 'XS', 'L', 'XL', 'XS', '2XL', 'XL', 'S', 'XS', '3XL', 'XS', 'L', 'S', 'M', '3XL', 'XL', 'S', 'XS', 'XS', '2XL', 'XS', 'S', 'M', 'M', '2XL', 'XL', 'M', 'XL', 'XS', '3XL', '2XL', 'L', 'XS', '3XL', 'M', 'XS', '3XL', '2XL', 'XS', '3XL', '3XL', '2XL', '3XL', 'S', 'M', 'XS', 'S', 'XS', 'L', '3XL', 'M', 'S', 'XS', 'S', 'L', '2XL', '3XL', 'XS', 'S', 'L', '2XL', '3XL', 'M', 'S', 'XL', 'XL', 'M', 'S', 'XL', 'L', 'XL', 'L', 'S', 'L', 'M', '2XL', 'XL', 'XS', 'XS', 'M', 'L', 'M', '3XL', 'S', 'S', 'S', '3XL', '2XL', 'XS', 'XL', 'M', 'M', 'XL', 'XL', 'L', 'XL', 'XS', 'XS', '3XL', 'XS', '3XL', '3XL', 'XS', 'S', 'XS', '3XL', '2XL', 'XS', 'S', 'S', 'M', 'S', 'XL', '2XL', 'XL', 'M', 'XS', '3XL', 'XS', 'L', '3XL', 'S', 'L', '2XL', 'M', '3XL', '2XL', 'S', 'M', 'XS', '3XL', 'S', 'S', '3XL', '2XL', 'XS', 'XL', 'L', 'M', 'XL', 'S', '2XL', 'M', '3XL', 'S', 'XS', '2XL', 'XS', '2XL', 'S', 'M', 'L', 'XL', '3XL', 'XS', 'XL', 'XL', 'L', 'L', 'XS', 'M', '3XL', '3XL', '3XL', 'M', '2XL', '2XL', 'M', '3XL', 'L', 'XL', 'S', '3XL', 'XL', '2XL', 'S', 'L', '2XL', 'XS', 'XL', '2XL', 'L', 'S', 'XL', 'M', 'S', '2XL', 'M', 'XS', 'XS', 'XL', 'XS', 'XL', '3XL', '2XL', 'S', 'L', 'M', 'S', 'L', '3XL', 'M', '2XL', 'L', '3XL', 'S', 'XS', 'S', '2XL', 'XS', 'XL', '2XL', 'S', 'M', '2XL', 'XL', 'XS', '2XL', '3XL', '2XL', 'XL', 'M', 'M', 'M', '3XL', 'S', 'XS', 'XS', 'XS', 'S', '2XL', '2XL', 'XS', 'M', 'XL', 'XS', 'S', 'M', 'XS', '2XL', 'M', 'XS', 'L', 'L', 'XL', 'XS', 'M', 'S', 'S', '2XL', 'S', 'L', '2XL', '3XL', 'M', 'M', 'M', 'XS', 'XS', 'L', 'S', '3XL', '3XL', 'M', 'S', 'XL', '2XL', 'M', 'S', 'S', 'M', '2XL', '3XL', 'M', 'S', '3XL', 'M', 'M', 'L', '3XL', '3XL', 'L', 'M', 'L', 'S', 'XS', 'XS', '3XL', 'XS', 'XL', 'S', '3XL', '2XL', 'M', 'XL', 'S', '2XL', 'XL', '2XL', 'L', 'S', 'S', 'M', 'L', 'XL', 'XL', '3XL', 'XS', '3XL', '2XL', 'S', 'L', 'XL', 'M', 'L', 'S', '2XL', 'M', 'XS', 'M', '2XL', 'XL', 'XS', '3XL', 'M', '2XL', 'L', 'L', '2XL', '2XL', 'L', '3XL', 'M', '2XL', 'XL', 'S', '2XL', 'XL', '3XL', '2XL', 'XS', 'M', 'L', 'L', 'L', 'XL', 'M', 'L', '2XL', '3XL', 'XL', 'XL', '3XL', '3XL', 'XS', '3XL', 'S', 'S', 'XL', 'L', '2XL', 'XL', 'L', '3XL', '3XL', 'XS', 'XL', 'XS', 'XL', '2XL', '3XL', 'XL', 'S', 'XS', '2XL', 'S', 'XS', 'M', '2XL', 'S', 'L', '3XL', 'S', 'XL', 'XL', 'M', 'M', 'L', 'M', 'XS', '2XL', 'XS', '3XL', 'M', '2XL', '2XL', 'L', 'M', 'XL', 'M', '3XL', 'S', '2XL', 'XS', 'M', 'S', 'L', '2XL', '3XL', 'M', '2XL', 'S', 'S', '2XL', '3XL', 'L', 'M', 'XS', 'XS', 'XS', '3XL', 'XS', 'S', '2XL', '3XL', '3XL', 'S', 'L', 'L', '2XL', 'M', 'L', 'L', 'XL', '3XL', 'M', 'S', 'M', 'XS', 'XS', 'L', 'L', 'M', 'S', 'XL', 'S', 'S', 'S', '3XL', '3XL', 'L', 'XL', 'XS', 'XL', 'XS', 'XS', 'M', 'M', '3XL', 'S', 'S', '2XL', 'L', '3XL', '2XL', '2XL', '2XL', 'M', '2XL', '3XL', 'XS', 'XS', 'XS', '2XL', 'L', 'XS', 'S', 'XS', '3XL', 'XL', 'S', 'M', '3XL', '2XL', 'XS', 'XS', 'M', 'S', 'XL', 'M', 'XS', 'M', 'XL', 'XL', 'XL', 'S', 'XS', '3XL', '2XL', 'XS', 'M', 'S', 'M', 'XS', 'XL', 'XL', '3XL', 'M', 'M', '2XL', 'L', 'S', 'XL', '3XL', 'M', 'XL', '2XL', 'XL', 'M', 'XS', '2XL', 'XS', 'XL', 'M', '3XL', 'XS', 'S', 'L', '3XL', 'XS', '3XL', 'S', 'L', '2XL', 'XL', 'XS', 'L', 'L', 'L', '2XL', 'S', 'L', 'S', 'S', '3XL', 'XL', 'XL', 'M', 'S', 'XS', 'L', 'S', '2XL', 'S', 'XL', 'L', '2XL', '2XL', 'M', 'L', '2XL', '3XL', 'S', 'XS', 'XS', '2XL', 'M', '3XL', 'M', 'XS', 'S', 'S', 'XS', '3XL', 'M', '2XL', '2XL', 'L', '3XL', 'L', 'XS', 'M', 'L', '2XL', 'XL', 'L', 'XS', 'XS', 'L', 'L', 'L', 'XL', 'XS', 'XL', 'M', '3XL', 'XL', '2XL', '3XL', 'M', 'S', 'S', '3XL', 'S', '2XL', 'XS', '3XL', '3XL', 'XS', 'M', 'M', 'XS', 'M', 'L', 'XS', '3XL', '2XL', 'S', 'L', 'S', 'XS', 'S', 'S', 'M', 'XL', '2XL', '2XL', 'L', '2XL', 'M', 'XL', 'XS', 'XL', 'M', 'M', '3XL', 'M', 'XS', 'L', '2XL', 'M', 'M', '3XL', 'L', '2XL', '2XL', 'XS', 'L', 'L', '3XL', 'XL', '2XL', '2XL', 'S', 'XL', 'L', 'XS', '3XL', 'S', 'L', 'XS', '2XL', 'S', 'S', '3XL', 'S', 'L']
size_result = Counter(result)
size_result = size_result.most_common()
size_result = list(zip(*size_result))
sizes = list(size_result[0])
size_counts = list(size_result[1])

total = len(male_ages) + len(female_ages)
ratio_f = len(female_ages)/total
ratio_m = 1 - ratio_f

# Calculate angles for pie chart

start_angles = []
start_angles.append(0)
start_angles.append(2*np.pi * ratio_f)

end_angles = []
end_angles.append(start_angles[1])
end_angles.append(2*np.pi)

# Data source for HBar

curdoc().theme = 'dark_minimal'

size_cds = ColumnDataSource(data=dict(sizes=sizes, counts=size_counts, color=Cividis[len(sizes)]))

fig1 = figure(title="Female ages", plot_width=400, plot_height=400)
fig1.quad(top=female_ages_hist, bottom=0, left=edges_f[:-1], right=edges_f[1:], fill_color="red", line_color="white", alpha=0.7)
fig1.xgrid.visible = False
fig1.ygrid.visible = False

fig2 = figure(title="Male ages", plot_width=400, plot_height=400)
fig2.quad(top=male_ages_hist, bottom=0, left=edges_m[:-1], right=edges_m[1:], fill_color="navy", line_color="white", alpha=0.7)
fig2.xgrid.visible = False
fig2.ygrid.visible = False

fig3 = figure(title="Female to male ratio", plot_width=400, plot_height=400)
colors = ["red", "blue"]
fig3.wedge(x=0, y=0, radius=0.75, start_angle=start_angles, end_angle=end_angles, color=colors, alpha=0.7)
fig3.xgrid.visible = False
fig3.xaxis.visible = False
fig3.ygrid.visible = False
fig3.yaxis.visible = False

fig4 = figure(y_range=sizes, title="Most common sizes", plot_width=400, plot_height=400)
fig4.hbar(y='sizes', right='counts', color='color', width=0.9, source=size_cds)

graph = gridplot([fig1, fig2, fig3, fig4], ncols=2)
show(graph)