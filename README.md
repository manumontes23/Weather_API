# Weather_API
endpoint get weather, flask

###### **Get weather**

**parameters:**
    _city:_ name of the city <String>
    _country:_ cod of the country, two characters
**response:**
    _location_name:_ city name and country code of two characters 
    _temperature:_ Temperature unit: Celsius
    _wind:_ description of the wild, wild speed and wild direction
    _cloudiness:_ description of the sky
    _pressure:_ Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
    _humidity:_ Humidity, %
    _sunrise:_ sunrise time
    _sunset:_ sunset time
    _geo_coordinates:_ City geo location [longitude, latitude]
    _requested_time:_ Time of the request
    _forecast:_ {..} empy dict


**how to run  the code:**
    -- on a python eviroment execute the command Flask run
    -- Use any browser to access http://127.0.0.1:5000/
