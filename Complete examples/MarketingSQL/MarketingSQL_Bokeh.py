import mysql.connector
from bokeh.io import show, curdoc
from bokeh.plotting import figure
from bokeh.themes import built_in_themes
from bokeh.layouts import gridplot
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Cividis
import numpy as np
from collections import Counter

def read_db(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def untuple(tuple_list):
    list = []
    for value in tuple_list:
        list.append(value[0])
    return list


connection = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Marketing")

query = "SELECT age FROM MARKETING_DATA where gender = 'F';"
result = read_db(query)
female_ages = untuple(result)
female_ages_hist, edges_f = np.histogram(female_ages, bins = 10)

query = "SELECT age FROM MARKETING_DATA where gender = 'M';"
result = read_db(query)
male_ages = untuple(result)
male_ages_hist, edges_m = np.histogram(male_ages, bins = 10)

query = "SELECT size FROM MARKETING_DATA;"
result = read_db(query)
size_result = Counter(untuple(result))
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

fig4 = figure(y_range = sizes, title="Most common sizes", plot_width=400, plot_height=400)
fig4.hbar(y='sizes', right='counts', color='color', width=0.9, source=size_cds)

graph = gridplot([fig1, fig2, fig3, fig4], ncols=2)
show(graph)