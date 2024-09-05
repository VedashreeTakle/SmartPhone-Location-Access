import tkinter
import tkintermapview
import phonenumbers 
import opencage

from phonenumbers import geocoder 
from phonenumbers import carrier 

from opencage.geocoder import OpenCageGeocode

from tkinter import *
from tkinter import messagebox 
import json
from urllib.request import urlopen

url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)

data.popitem()
data.pop('org')
new_data=str(data)
location=data.get("loc")
loc_list = [float(coord) for coord in location.split(',')]
city_name=data.get("city")
latitude = loc_list[0]
longitude = loc_list[1]

root = tkinter.Tk()
root.geometry("500x500")

key = "dafe51e06f4b41f1be64c4c7f2344862" #opencage API

label1 = Label(text="Phone Number Tracker")
label1.pack()

label2 = Label(text="Enter phone number with country code")
label2.pack()

def getResult():
    num= number.get("1.0", END)
    num1 = phonenumbers.parse(num)

    location = geocoder.description_for_number(num1, "en")
    service = carrier.name_for_number(num1, "en")

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=1)
    map_widget.set_position(latitude,longitude)
    map_widget.set_marker(latitude, longitude, text="Phone Found")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()

    adr = tkintermapview.convert_coordinates_to_address(lat,lng)

    result.insert(END,"The country of this number is : "+location)
    result.insert(END,"\nThe sim card company of this number is : "+service)
    result.insert(END,"\n Latitude is : "+str(lat))
    result.insert(END,"\n Longitude is : "+str(lng))
    result.insert(END,"\nThe city of this number's sim card is : "+city_name)

number=Text(height=1)
number.pack()

button = Button(text="Search", command=getResult)
button.pack(pady=10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()