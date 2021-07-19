from flask import Flask, request
import requests
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome!"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', default=None)
    country = request.args.get('country', default=None)
    try:
        resp = get_info_openweather(city, country)
        if resp.status_code == 200:      
            return formating(resp.json())
        else:
            return resp
    except:
        return "Error"

def get_info_openweather(city, country):
    return requests.get('https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032'.format(city=city, country=country))

def formating(resp):
    res_format ={"location_name": resp["name"] + ", " + resp["sys"]["country"],
                 "temperature": str(round(resp["main"]["temp"] - 273.15,0)) + " °C",
                 "wind": resp["wind"],
                  "cloudiness": resp["weather"][0]["description"],
                 "pressure": str(resp["main"]["pressure"]) + "hpa",
                 "humidity": str(resp["main"]["humidity"]) + "%",
                 "sunrise": time.strftime("%H:%M",time.gmtime(resp["sys"]["sunrise"])),
                 "sunset": time.strftime("%H:%M",time.gmtime(resp["sys"]["sunset"])),
                 "geo_coordinates": [resp["coord"]["lon"],resp["coord"]["lat"]],
                 "requested_time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(resp["dt"])),
                 "forecast": {}
                 }
    return res_format

'''
 Return description of the wind using Beaufort scale
 parameters:
    speed : double
    the speed of the wind, unit m/s
'''
def wind_description(speed):
    if speed < 0.5:
        description = "Calm"   
    elif speed <= 1.5:
        description = "Light air"
    elif speed <= 3.3:
        description = "Light breeze"  
    elif speed <= 5.5:
        description = "Gentle breeze"
    elif speed <= 7.9:
        description = "Moderate breeze"
    elif speed <= 10.7:
        description = "Fresh breeze"
    elif speed <= 13.8:
        description = "Strong breeze"
    elif speed <= 17.1:
        description = "High wind"
    elif speed <= 20.7:
        description = "Gale"
    elif speed <= 24.4:
        description = "Strong gale"
    elif speed <= 28.4:
        description = "Storm"
    elif speed <= 32.6:
        description = "Violent Storm"
    else:
        description = "Hurricane"
    return description