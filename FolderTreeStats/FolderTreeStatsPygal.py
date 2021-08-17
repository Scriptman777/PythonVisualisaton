import os
import tkinter as tk
import pygal
from pygal.style import DarkStyle
from tkinter import filedialog
  
def get_size(path, subdirs):
    size = 0
    for element in os.scandir(path):
        if element.is_dir() and subdirs:
            size += get_size(element.path,True)
        elif element.is_file():
            size += element.stat().st_size

    return size

def get_subdirs(path):
    list = []
    for dir in os.listdir(path):
        item = path + '/' + dir
        if os.path.isdir(item):
            list.append(item)
    return list




root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
 
subdirs = get_subdirs(file_path)

treemap = pygal.Treemap(value_formatter=lambda x: '{:.2f}MB'.format(x), style=DarkStyle)

treemap.add(os.path.basename(file_path), [{'value' : get_size(file_path,False)/1000000, 'label': file_path}])

for dir in subdirs:
    bottom_dirs = get_subdirs(dir)
    bot_values = []
    for bot_dir in bottom_dirs:
        print(bot_dir)
        bot_values.append({'value' : get_size(bot_dir,True)/1000000, 'label': bot_dir})
    bot_values.append({'value' : get_size(dir,False)/1000000, 'label': dir})
    treemap.add(os.path.basename(dir),bot_values)


treemap.render_to_file('map.svg')
    


