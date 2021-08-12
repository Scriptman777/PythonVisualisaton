from bokeh.plotting import figure
from bokeh.io import show, curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource
from bokeh.server.server import Server
import random
import time
import psutil
import GPUtil

def update():
    
    new_data_cpu = {
    'percent' : [psutil.cpu_percent()],
    'time' : [time.time()],
    }

    source_cpu.stream(new_data_cpu,50)

    new_data_mem_v = {
    'percent' : [psutil.virtual_memory().percent],
    'time' : [time.time()],
    }

    source_mem_v.stream(new_data_mem_v,50)

    new_data_net_out = {
    'packets' : [psutil.net_io_counters().packets_sent],
    'time' : [time.time()],
    }

    network_sent.stream(new_data_net_out,100)

    new_data_net_in = {
    'packets' : [psutil.net_io_counters().packets_recv],
    'time' : [time.time()],
    }

    network_recived.stream(new_data_net_in,100)

    gpus = GPUtil.getGPUs()
    gpu = gpus[0]

    new_data_gpu_use = {
    'percent' : [gpu.load*100],
    'time' : [time.time()],
    }

    gpu_usage.stream(new_data_gpu_use,50)

    new_data_gpu_temp = {
    'temp' : [gpu.temperature],
    'time' : [time.time()],
    }

    gpu_temp.stream(new_data_gpu_temp,50)





source_cpu = ColumnDataSource(data=dict(time=[],percent=[]))
source_mem_v = ColumnDataSource(data=dict(time=[],percent=[]))

network_sent = ColumnDataSource(data=dict(time=[],packets=[]))
network_recived = ColumnDataSource(data=dict(time=[],packets=[]))

gpu_usage = ColumnDataSource(data=dict(time=[],percent=[]))
gpu_temp = ColumnDataSource(data=dict(time=[],temp=[]))

p_cpu = figure(plot_width=800, plot_height=400, title="CPU usage %", y_range=(0, 100))
p_cpu.line(x='time', y='percent', source=source_cpu, line_width=2, line_color="blue", fill_color="blue", fill_alpha=0.3)
p_cpu.xaxis.visible = False

p_mem_v = figure(plot_width=800, plot_height=400, title="Virtual memory usage %", y_range=(0, 100))
p_mem_v.line(x='time', y='percent', source=source_mem_v, line_width=2, line_color="white")
p_mem_v.xaxis.visible = False

p_net_out = figure(plot_width=800, plot_height=400, title="Network: total packets sent")
p_net_out.line(x='time', y='packets', source=network_sent, line_width=2, line_color="lightblue")
p_net_out.xaxis.visible = False

p_net_in = figure(plot_width=800, plot_height=400, title="Network: total packets recived")
p_net_in.line(x='time', y='packets', source=network_recived, line_width=2, line_color="orange")
p_net_in.xaxis.visible = False

p_gpu_use = figure(plot_width=800, plot_height=400, title="GPU usage %")
p_gpu_use.line(x='time', y='percent', source=gpu_usage, line_width=2, line_color="green")
p_gpu_use.xaxis.visible = False

p_gpu_temp = figure(plot_width=800, plot_height=400, title="GPU temperature")
p_gpu_temp.line(x='time', y='temp', source=gpu_temp, line_width=2, line_color="red")
p_gpu_temp.xaxis.visible = False


curdoc().theme = 'dark_minimal'
curdoc().add_periodic_callback(update, 100)
curdoc().add_root(column(row(p_cpu, p_mem_v), row(p_net_out, p_net_in), row(p_gpu_use, p_gpu_temp)))
curdoc().title = "HW Usage"


# bokeh serve --show path_to_file\BokehStreaming.py

# bokeh serve --show E:\Users\Dokumenty\FIM\BC\BCWork\BokehStreaming\BokehStreaming.py