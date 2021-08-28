import holoviews as hv
import pandas as pd
from bokeh.io import show
from bokeh.layouts import gridplot
import csv

hv.extension('bokeh')

complete_df = pd.read_csv('heart_rate.csv')

df = complete_df[['com.samsung.health.heart_rate.start_time','com.samsung.health.heart_rate.heart_rate']]
df = df.rename(columns={"com.samsung.health.heart_rate.start_time": "Date", "com.samsung.health.heart_rate.heart_rate": "Heart Rate"}).sort_values(by=['Date'])

graph = hv.Curve(df).opts(width=800, height=500, xrotation=90, color='red')

hv.save(graph, 'plot.html', backend='bokeh')