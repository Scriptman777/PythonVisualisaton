import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import tkinter as tk
from tkinter import filedialog
import glob
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

list = glob.glob(file_path + "/*.wav")

plot_amount = len(list)*2
current_axis = 0
fig_y = plot_amount*3
fig, axs = plt.subplots(plot_amount, 1, figsize=(10,fig_y))
plt.tight_layout(pad=3.0)

for sound in list:
    try:
        audio, sample_rate = librosa.load(sound)
        stft = librosa.stft(audio)
        a_to_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    except :
        print("Error processing file: " + os.path.basename(sound))
        continue

    librosa.display.specshow(a_to_db, ax=axs[current_axis])
    axs[current_axis].set(title="Spectrograph for file: " + os.path.basename(sound))
    current_axis = current_axis + 1

    librosa.display.waveplot(audio, sample_rate, ax=axs[current_axis])
    axs[current_axis].set(title="Waveform for file: " + os.path.basename(sound))
    current_axis = current_axis + 1

    
    print("Processed file " + str(int(current_axis/2)) + "/" + str(len(list)))

pdf = PdfPages('Music Analysis.pdf')
pdf.savefig()

pdf.close()

os.startfile('Music Analysis.pdf')

