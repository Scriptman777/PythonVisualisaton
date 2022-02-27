import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import tkinter as tk
from tkinter import filedialog
import glob
import os

# GET DATA

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

# Get all wav files
list = glob.glob(file_path + "/*.wav")

# Prepare plots for visualisation
plot_amount = len(list)*2
current_axis = 0
fig_y = plot_amount*3
fig, axs = plt.subplots(plot_amount, 1, figsize=(10,fig_y))
plt.tight_layout(pad=3.0)

# PROCESS DATA

for sound in list:
    try:
        # Get audio
        audio, sample_rate = librosa.load(sound)
        # Perform short-time Fourier transform
        stft = librosa.stft(audio)
        # Get db from amplitude
        a_to_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    except :
        print("Error processing file: " + os.path.basename(sound))
        continue

    # VISUALIZE DATA

    # Create graph for spectrograph
    librosa.display.specshow(a_to_db, ax=axs[current_axis])
    axs[current_axis].set(title="Spectrograph for file: " + os.path.basename(sound))
    current_axis = current_axis + 1

    # Create graph for waveform
    librosa.display.waveplot(audio, sample_rate, ax=axs[current_axis])
    axs[current_axis].set(title="Waveform for file: " + os.path.basename(sound))
    current_axis = current_axis + 1

    # Inform user in console about status, since the processing might take some time
    print("Processed file " + str(int(current_axis/2)) + "/" + str(len(list)))

# Export all graphs as PDF
pdf = PdfPages('Music Analysis.pdf')
pdf.savefig()

pdf.close()

# Open created file
os.startfile('Music Analysis.pdf')

