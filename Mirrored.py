#!/usr/bin/env python
from tkinter import *
import time
import requests
import json

#inputs
#weather_api_token = 'XXX'
#weather_unit = 'us'
#ip = 'XXX' #Get a new one for the Apartment
#google_api = 'XXX'


"""Icon Lookup"""
icon_lookup = {
    'cloudy': r'/Users/USERNAME/Desktop/Mirror/icons/icon:cloudy.gif',
    'wind': r'/Users/USERNAME/Desktop/Mirror/icons/icon:wind.gif',
    'clear-day': r'/Users/USERNAME/Desktop/Mirror/icons/icon:clear-day.gif',
    'clear-night': r'/Users/USERNAME/Desktop/Mirror/icons/icon:clear-night.gif',
    'partly-cloudy-day':r'/Users/USERNAME/Desktop/Mirror/icons/icon:partly-cloudy-day.gif',
    'partly-cloudy-night': r'/Users/USERNAME/Desktop/Mirror/icons/icon:partly-cloudy-night.gif',
    'snow':r'/Users/USERNAME/Desktop/Mirror/icons/icon:snow.gif',
    'snow-thin':r'/Users/USERNAME/Desktop/Mirror/icons/icon:snow-thin.gif',
    'rain': r'/Users/USERNAME/Desktop/Mirror/icons/icon:rain.gif',
    'thunderstorm': r'/Users/USERNAME/Desktop/Mirror/icons/icon:thundersorm.gif',
    'hail': r'/Users/USERNAME/Desktop/Mirror/icons/icon:hail.gif',
    'fog': r'/Users/USERNAME/Desktop/Mirror/icons/icon:fog.gif',
    'tornado': r'/Users/USERNAME/Desktop/Mirror/icons/icon:tornado.gif'

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
        self.icon_spot = ''
        self.conditions_spot = ''
        self.temp_spot = ''
        self.current_icon = Label(master, fg='white', bg='black', text=self.icon_spot)
        self.current_icon.pack(ipady=10, anchor=SW, expand=NO)
        self.current_conditions = Label(master, font=("Helvetica", 30), fg='white', bg='black', text=self.conditions_spot)
        self.current_conditions.pack(anchor=SW, expand=NO)
        self.current_temp = Label(master, font=("Helvetica",50), fg='white', bg='black', text = self.temp_spot)
        self.current_temp.pack(anchor=SW, expand=NO)
        self.tock()
        

    def tock(self):
        r = requests.get('https://api.darksky.net/forecast/53ab19cfa7d75e3012b1767a35e8057b/40.825901,-74.209005')
        weather_obj = json.loads(r.text)
        degree_sign = u'\N{DEGREE SIGN}'

        conditions_id = weather_obj['currently']['summary']
        temp_id = "%s%s" % (int(weather_obj['currently']['temperature']), degree_sign)
        icon_id = weather_obj['currently']['icon']
        icon = PhotoImage(file=icon_lookup[weather_obj['currently']['icon']])
        if temp_id != self.temp_spot:
            self.temp_spot = temp_id
            self.current_temp.config(text=temp_id)
        if conditions_id != self.conditions_spot:
            self.conditions_spot = conditions_id
            self.current_conditions.config(text=conditions_id)
        if self.icon_spot != icon_id:
            self.current_icon.config(image=icon)
            self.current_icon.image = icon
            self.icon_spot = icon_id
        self.after(60000, self.tock)


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
