import requests
import pygame
from miditime.miditime import MIDITime

# GET DATA

# Get data from REST API
request = requests.get("https://worldweather.wmo.int/en/json/197_en.json")
res_json = request.json()
forecasts = res_json['city']['forecast']

temps = []

# PROCESS DATA

# Create a list of temperatures for the following days
for forecast in forecasts['forecastDay']:
    temps.append(forecast['minTemp'])

# Initialize a MIDI file
mymidi = MIDITime(120, 'weather.mid')

notes = []
beat = 0

# Add data as notes
for temp in temps:
    notes.append([beat,int(temp) + 60,100,1])
    beat += 1

# VISUALIZE DATA

# Save MIDI
mymidi.add_track(notes)
mymidi.save_midi()

# Play notes from MIDI
pygame.init()

pygame.mixer.music.load("weather.mid")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)


