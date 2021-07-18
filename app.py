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
    resp = get_info_openweather(city, country)
    return formating(resp)

def get_info_openweather(city, country):
    return requests.get('https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032'.format(city=city, country=country))

def formating(resp):
    res_format ={"location_nme": resp["name"] + ", " + resp["sys"]["country"],
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