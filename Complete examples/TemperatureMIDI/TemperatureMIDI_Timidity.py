import requests
import timidity
import scipy.signal as sig
from miditime.miditime import MIDITime

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

ps = timidity.Parser('weather.mid')


timidity.play_notes(*ps.parse(), sig.sawtooth)