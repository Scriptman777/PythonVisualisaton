import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sciwave


fig, axs = plt.subplots(3,1,figsize =(8, 8))
plt.tight_layout(pad=3.0)

# Load sound from file with sample rate
audio, sample_rate = librosa.load("sheep.wav")
# Short time Fourier transform
stft = librosa.stft(audio)
# Create spectrogram
a_to_db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)

# Load with SciPy
sc_rate, sc_audio = sciwave.read("sheep.wav")
# X axis for chart
sc_x = np.linspace(0,len(sc_audio),len(sc_audio))

# Visualize
librosa.display.waveshow(audio, ax=axs[0])
axs[0].set_title("Librosa waveshow")
librosa.display.specshow(a_to_db, ax=axs[1])
axs[1].set_title("Librosa specshow")
axs[2].scatter(sc_x, sc_audio, s=0.5)
axs[2].set_title("SciPy scatter")
plt.show()