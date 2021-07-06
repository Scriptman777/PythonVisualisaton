import requests
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("https://trackmania.exchange/api/replays/get_replays/26483/25")
print(response)

resJson = response.json()

drivers = []
times = []
for data in resJson:
    drivers.append(data.get('Username'))
    times.append(data.get('ReplayTime'))

fig = plt.figure(figsize = (16, 9))

plt.barh(drivers,times)

plt.show()

