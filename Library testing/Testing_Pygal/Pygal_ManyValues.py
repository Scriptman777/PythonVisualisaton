import pandas as pd
import numpy as np
import pygal
from pygal.style import Style, DarkGreenStyle

# Sample data

data = pd.read_csv('MOCK_DATA.csv')

x = np.linspace(0,2*np.pi,50)
sin_x = np.sin(x)
cos_x = np.cos(x)
sin_2x = np.sin(2*x)
cos_x_2 = np.cos(x)*2
sqrt_x = np.sqrt(x)

funcs = [sin_x, cos_x, sin_2x, cos_x_2, sqrt_x]
func_names = ['sin_x', 'cos_x', 'sin_2x', 'cos_x_2', 'sqrt_x']

# Line plot

line = pygal.Line()
line.x_labels = x
index = 0
for func in funcs:
    line.add(func_names[index], func)
    index += 1

line.show_legend = False
line.render_in_browser()

# Scatter plot

scatter = pygal.XY(stroke=False)
index = 0
for func in funcs:
    scatter_points = []
    value_list = func.tolist()
    for value in value_list:
        index = value_list.index(value)
        scatter_points.append((x[index], value))
    scatter.add('Function values', scatter_points)
    index += 1

scatter.show_legend = False
scatter.render_in_browser()

# Bar plot

bar = pygal.Bar(x_label_rotation=35)

profits = data['profit'].tolist()
exchanges = data['exchange'].tolist()
companies = data['company'].tolist()
employees = data['employees'].tolist()
category = data['arbitraryCategory'].tolist()

for company in companies:
    index = companies.index(company)
    bar.add(company, [{'value': profits[index], 'label': 'Exchange: {exc} | Employees: {empl} | Category: {cat}'.format(exc=exchanges[index], empl=employees[index], cat=category[index])}])

bar.show_legend = False
bar.render_in_browser()
