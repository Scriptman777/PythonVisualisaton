import os
import tkinter as tk
from tkinter import filedialog
  

def get_size(path):
    size = 0
    for element in os.scandir(path):
        if element.is_file():
            size += element.stat().st_size
        elif element.is_dir():
            size += get_size(element.path)

    return size

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
  
  
dirsize = get_size(file_path)
     
print(dirsize)