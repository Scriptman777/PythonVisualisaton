import holoviews as hv
import pandas as pd
from bokeh.io import show
from bokeh.layouts import gridplot
import csv

hv.extension('bokeh')

complete_heart_df = pd.read_csv('heart_rate.csv')
df_heart = complete_heart_df[['com.samsung.health.heart_rate.start_time','com.samsung.health.heart_rate.heart_rate']]
df_heart = df_heart.rename(columns={"com.samsung.health.heart_rate.start_time": "Date", "com.samsung.health.heart_rate.heart_rate": "Heart Rate"}).sort_values(by=['Date'])

complete_oxy_df = pd.read_csv('oxygen.csv')
df_oxy = complete_oxy_df[['com.samsung.health.oxygen_saturation.start_time','com.samsung.health.oxygen_saturation.spo2']].rename(columns={"com.samsung.health.oxygen_saturation.start_time": "Date", "com.samsung.health.oxygen_saturation.spo2": "O2"}).sort_values(by=['Date'])

#axiswise attribute needed to not contaminate the other axis
graph_heart = hv.Curve(df_heart).opts(width=800, height=500, xrotation=90, color='red', axiswise=True)
graph_oxy = hv.Bars(df_oxy).opts(width=800, height=500, xrotation=90, axiswise=True)

layout = graph_heart + graph_oxy

hv.save(layout, 'plot.html', backend='bokeh')