from tkinter import *
from unicodedata import category
import requests
import json
from urllib.request import urlretrieve


root = Tk()
root.title("Code")
root.geometry('600x100')

def zip_func():

    try:

        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zip.get() +'&distance=25&API_KEY=F9B9AD5F-2E21-40C5-87B7-5F256D990AC2')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            colour = 'green'
        elif category == "Moderate":
            colour = "yellow"
        elif category == "Unhealthy for Sensitive Groups":
            colour = 'orange'
        elif category == "Unheathy":
            colour = "red"
        elif category == "Very unhealthy":
            colour = 'purple'
        elif category == "Harzardous":
            colour = "7e0023"
        
        root.configure(background = colour)

        mylab = Label(root,text = city + " Air Quality " + str(quality) + " " + category, font = ('Helvetica',20), background=colour)
        mylab.grid(row = 1,column = 0,columnspan = 2)

    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row = 0 , column= 0 , stick = N+E+W+S)

but = Button(root,text="Lookup Zipcode",command=zip_func)
but.grid(row = 0 , column= 1,stick = N+E+W+S)

root.mainloop()
