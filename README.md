   ![mirror_example](https://cloud.githubusercontent.com/assets/24977834/25873200/2b841d88-34d3-11e7-98ba-59433cea3cdd.JPG)

# Smart-Mirror-Project
As a learning experience, I developed a smart-mirror python program for a raspberri pi hardwired into an LCD monitor behind a two-way mirror. The idea is to have a regular decorative household mirror that also displays meaningful information like weather, time, news, and current commute time between the mirror and work.

If you'd like to implement this onto a raspberri pi, a few things you'll need is the Tkinter library as well as some way to get JSON information. I use requests.

Notice in the 'icons' folder I have duplicate icons in different file formats. For whatever reason, PIL was not working for me so I could not use the ImageTk module to get PNG files to work, so to get around that I simply reformated my PNG icons to GIF files and it works just fine without importing from the PIL library. 

I intend to outfit another API here, feel free to comment on what kinds of information might be useful on a day-to-day smart mirror. I'm thinking either news or an animated .gif of carlton doing his dance on the bottom corner. 


# UPDATE: 2/18/2017
I added a request to the Google Traffic API and displays the current estimated time of travel between one location and another. To input addresses into the 'origin' and 'destination' parameters in the url, Google makes it easy by simply typing in the address like a concatenated string. Example: 'origin=100+6th+Avenue+New+York+NY+10001'. The same works for destinations. You can also use Lat and Long coordinates. Make sure every parameter is separated by the '&', and go to https://developers.google.com/maps/documentation/distance-matrix/start to get your API key, which goes at the very end of the URL. 
