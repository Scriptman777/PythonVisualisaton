import requests
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def create_plot(track_id):
    response_times = requests.get("https://trackmania.exchange/api/replays/get_replays/" + track_id + "/25")
    response_track = requests.get("https://trackmania.exchange/api/tracks/get_track_info/multi/" + track_id)
    print(response_times)

    res_json = response_times.json()
    res_json_track = response_track.json()

    track_name = res_json_track[0].get('Name')

    drivers = []
    times = []
    colors = ['goldenrod', 'silver', 'peru']

    for x in range (0,len(res_json)-3):
        colors.append('gray')

    for data in res_json:
        drivers.append(data.get('Username'))
        times.append((data.get('ReplayTime'))/1000)



    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(drivers,times, color=colors)
    ax.invert_yaxis()
    ax.set_title('Best times for the track: ' + track_name)

    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                 str(i.get_width()),
                 fontsize = 10, fontweight ='bold',
                 color ='grey')

    plt.show()



window = tk.Tk()
window.geometry("300x100")
tk.Label(window, text="Please enter the Trackmania Exchange track ID:").grid(row=0)

field_id = tk.Entry(window)
field_id.grid(row=1, column=0)

tk.Button(window, text="Go", command=lambda: create_plot(field_id.get())).grid(row=2)
window.mainloop()



