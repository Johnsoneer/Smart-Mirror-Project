#!/usr/bin/env python
from tkinter import *
import time
import requests
import json

#inputs
#weather_api_token = '53ab19cfa7d75e3012b1767a35e8057b'
#weather_unit = 'us'
#ip = '173.63.112.239' #Get a new one for the Apartment
#google_api = 'AIzaSyAXWyIIHISHL3U7-lkQO3rgXS-CO_7v-GE'
r = requests.get('https://api.darksky.net/forecast/53ab19cfa7d75e3012b1767a35e8057b/40.825901,-74.209005')
weather_obj = json.loads(r.text)
degree_sign = u'\N{DEGREE SIGN}'
rm = requests.get('https://maps.googleapis.com/maps/api/staticmap?center=Australia&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=AIzaSyAXWyIIHISHL3U7-lkQO3rgXS-CO_7v-GE')
#map_obj = json.loads(rm.image)

"""Icon Lookup"""
icon_lookup = {
    'cloudy': 'icon:cloudy.png',
    'wind': 'icon:wind.png',
    'clear-day': 'icon:clear-day.png',
    'clear-night': 'icon/clear-night.png',
    'partly-cloudy-day':'icon:partly-cloudy-day.png',
    'partly-cloudy-night':'icon:partly-cloudy-night.png',
    'snow':'icon:snow.png',
    'snow-thin':'icon:snow-thin.png',
    'rain': 'icon:rain.png',
    'thunderstorm': 'icon:thundersorm.png',
    'hail': 'icon:hail.png',
    'fog': 'icon:fog.png',
    'tornado': 'icon:tornado.png'

}

"""CLOCK"""
class Clock(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, bg='black')
        self.time1 = ''
        self.clock = Label(master, font=("Helvetica", 70), fg='white', bg='black', text=self.time1)
        self.clock.pack(fill=BOTH, expand=YES)
        self.tick()
            # Clock self-updates

    def tick(self):
        time2 = time.strftime('%I:%M')
        if time2 != self.time1:
            self.time1 = time2
            self.clock.config(text=time2)
        # calls itself every 200 milliseconds
        self.clock.after(200, self.tick)


"""WEATHER"""
class Weather(Frame):



    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, bg='black')
        self.icon = PhotoImage(file=icon_lookup[weather_obj['currently']['icon']])
        self.icon.pack(ipady=10, anchor=SW, expand=NO)
        #self.current_icon = Lable(master, font='Helvetica', fg='white', bg='black', text=weather_obj['currently']['summary'])
        #self.current_icon.pack(ipady=10, anchor=SW, expand=NO)
        self.current_conditions = Label(master, font=("Helvetica", 50), fg='white', bg='black', text=weather_obj['currently']['summary'])
        self.current_conditions.pack(anchor=SW, expand=NO)
        self.current_temp = Label(master, font=("Helvetica",80), fg='white', bg='black', text = "%s%s" % (int(weather_obj['currently']['temperature']), degree_sign))
        self.current_temp.pack(anchor=SW, expand=NO)

    icon_id = weather_obj['currently']['icon']
    #new_icon = PhotoImage(file=icon_lookup[icon_id])





"""MAPS(WIP)"""
class Maps(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, bg='black')
        pass

"""WINDOW"""
class FullScreen:
    def __init__(self):
        #Definitions: setting up the window
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topframe = Frame(self.tk, bg='black')
        self.topframe.pack(side=TOP, fill=BOTH, expand=NO)
        self.bottomframe = Frame(self.tk, bg='black')
        self.bottomframe.pack(side=BOTTOM, fill=BOTH, expand=NO)
        self.tk.bind("<Return>", self.Toggle_Full)
        self.tk.bind("<Escape>", self.end_full)
        self.check = False
        #clock
        self.clock = Clock(self.topframe)
        self.clock.pack(side=TOP)
        #Weather
        self.weather = Weather(self.bottomframe)
        self.weather.pack()

    def Toggle_Full(self, event=None):
        self.check = not self.check
        self.tk.attributes("-fullscreen", self.check)
        return 'break'

    def end_full(self, event=None):
        self.check = False
        self.tk.attributes('-fullscreen', False)
        return 'break'


"""CLOSING LOOP"""
a = FullScreen()
a.tk.mainloop()