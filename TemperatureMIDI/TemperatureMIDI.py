import requests
import pygame
from miditime.miditime import MIDITime
from pretty_midi import PrettyMIDI

request = requests.get("https://worldweather.wmo.int/en/json/197_en.json")
res_json = request.json()
forecasts = res_json['city']['forecast']

temps = []

for forecast in forecasts['forecastDay']:
    temps.append(forecast['minTemp'])

mymidi = MIDITime(120, 'weather.mid')

notes = []
beat = 0

for temp in temps:
    notes.append([beat,int(temp) + 60,100,1])
    beat += 1

mymidi.add_track(notes)
mymidi.save_midi()

pygame.init()

pygame.mixer.music.load("weather.mid")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)