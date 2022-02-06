import holoviews as hv
import numpy as np
from holoviews import dim
import pandas as pd
from bokeh.io import show
from bokeh.layouts import gridplot
import csv
import glob
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox

def fix_csv(csv):
    file = open(csv, 'r+')
    
    all_lines = file.readlines()
    del all_lines[0]
    for index in range(1,len(all_lines)):
        all_lines[index] = all_lines[index][:-2] + '\n'
    file.seek(0)
    file.writelines(all_lines)
    file.truncate()
    file.close()

def get_csv(name, list):
    for csv_file in list:
        if str(name) in csv_file:
            return csv_file
    return None

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

list = glob.glob(file_path + "/*.csv")

hv.extension('bokeh')

heart_csv = get_csv('com.samsung.shealth.tracker.heart_rate',list)
oxygen_csv = get_csv('com.samsung.shealth.tracker.oxygen_saturation',list)
step_csv = get_csv('com.samsung.shealth.tracker.pedometer_day_summary',list)

graphlist = []

if heart_csv is not None:
    try:
        complete_heart_df = pd.read_csv(heart_csv)
        df_heart = complete_heart_df[['com.samsung.health.heart_rate.start_time','com.samsung.health.heart_rate.heart_rate']]
        df_heart = df_heart.rename(columns={"com.samsung.health.heart_rate.start_time": "Date", "com.samsung.health.heart_rate.heart_rate": "Heart Rate"}).sort_values(by=['Date'])
        df_heart['Date'] = pd.to_datetime(df_heart['Date'])
    except pd.errors.ParserError:
        fix_csv(heart_csv)
        complete_heart_df = pd.read_csv(heart_csv)
        df_heart = complete_heart_df[['com.samsung.health.heart_rate.start_time','com.samsung.health.heart_rate.heart_rate']]
        df_heart = df_heart.rename(columns={"com.samsung.health.heart_rate.start_time": "Date", "com.samsung.health.heart_rate.heart_rate": "Heart Rate"}).sort_values(by=['Date'])
        df_heart['Date'] = pd.to_datetime(df_heart['Date'])
    #axiswise attribute needed to not contaminate the other axis
    graphlist.append(hv.Scatter(df_heart).opts(width=1000, height=500, xrotation=90, color='red', axiswise=True, size=dim('Heart Rate')/10))

if oxygen_csv is not None:
    try:
        complete_oxy_df = pd.read_csv(oxygen_csv)
        df_oxy = complete_oxy_df[['com.samsung.health.oxygen_saturation.start_time','com.samsung.health.oxygen_saturation.spo2']].rename(columns={"com.samsung.health.oxygen_saturation.start_time": "Date", "com.samsung.health.oxygen_saturation.spo2": "O2"}).sort_values(by=['Date'])
    except pd.errors.ParserError:
        fix_csv(oxygen_csv)
        complete_oxy_df = pd.read_csv(oxygen_csv)
        df_oxy = complete_oxy_df[['com.samsung.health.oxygen_saturation.start_time','com.samsung.health.oxygen_saturation.spo2']].rename(columns={"com.samsung.health.oxygen_saturation.start_time": "Date", "com.samsung.health.oxygen_saturation.spo2": "O2"}).sort_values(by=['Date'])
    #axiswise attribute needed to not contaminate the other axis
    graphlist.append(hv.Bars(df_oxy).opts(width=1000, height=500, xrotation=90, axiswise=True))

if step_csv is not None:
    try:
        complete_step_df = pd.read_csv(step_csv)
        df_step = complete_step_df[['create_time','step_count']].rename(columns={"create_time": "Date", "step_count": "Steps"}).sort_values(by=['Date'])
        df_step['Date'] = pd.to_datetime(df_step['Date'])
    except pd.errors.ParserError:
        fix_csv(step_csv)
        complete_step_df = pd.read_csv(step_csv)
        df_step = complete_step_df[['create_time','step_count']].rename(columns={"create_time": "Date", "step_count": "Steps"}).sort_values(by=['Date'])
        df_step['Date'] = pd.to_datetime(df_step['Date'])
    #axiswise attribute needed to not contaminate the other axis
    graphlist.append(hv.Scatter(df_step).opts(width=1000, height=500, xrotation=90, color='green', axiswise=True, size=np.log10(dim('Steps'))).hist()) 
    
if graphlist:
    layout = hv.Layout(graphlist).cols(1)

    hv.save(layout, 'plot.html', backend='bokeh')

    webbrowser.open('plot.html')
else:
    messagebox.showerror('ERROR','No graph could be created from supplied data')

