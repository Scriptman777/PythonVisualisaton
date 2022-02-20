import PIL.Image
import tkinter as tk
from tkinter import filedialog
import glob
import matplotlib.pyplot as plt
import numpy as np

# GET DATA

# Select folder containing photos with a simple directory dialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

# Select all .jpg files from the folder

list = glob.glob(file_path + "/*.jpg")

focal_lengths = np.array([], dtype=float)

# Read focal lengths for all photos

for path in list:
    img = PIL.Image.open(path)
    exif_data = img._getexif()
    focal_lengths = np.append(focal_lengths, float(exif_data[41989]))


bins_list = [0,22,25.5,27,29,31,39,41,49,51,70,110,130,150,180,220,280,320,380,450,600,800]

# VISUALIZE DATA

# Create plot
fig, axs = plt.subplots(figsize =(16, 9))
n, bins, patches = axs.hist(focal_lengths, bins = bins_list)

bin_centers = 0.5 * (bins[:-1] + bins[1:])

# Color the graph elements
cm = plt.cm.get_cmap('Greys')
col = bin_centers - min(bin_centers)
col = col/max(col)

for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c+0.25))

plt.margins(x=0)
plt.show()
