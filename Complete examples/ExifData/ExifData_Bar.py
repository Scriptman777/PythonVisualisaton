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

# PROCESS DATA

# Create a histogram object with NumPy
bins_list = [0,22,25.5,27,29,31,39,41,49,51,70,110,130,150,180,220,280,320,380,450,600,800]
bin_names = ["0 - 22", "22 - 25,5", "25,5 - 27", "27 - 29", "29 - 31", "31 - 39", "39 - 41", "41 - 49", "49 - 51", "51 - 70", "70 - 110", "110 - 130", "130 - 150", "150 - 180", "180 - 220", "220 - 280", "280 - 320", "320 - 380", "380 - 450", "450 - 600", "600 - 800"]

histogram = np.histogram(focal_lengths, bins_list)

# VISUALIZE DATA

# Use simple bar plot to visualize the histogram
fig, ax = plt.subplots(figsize =(16, 9))
ax.bar(bin_names, histogram[0], edgecolor="black", color="gray", width=1)
fig.autofmt_xdate()


plt.show()
