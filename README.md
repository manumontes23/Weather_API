# Weather_API
endpoint get weather, flask

###### **Get weather**

**parameters:**<br/><br/>
    -_city:_ name of the city <String> <br/>   
    -_country:_ cod of the country, two characters <br/> <br/>
    
**response:** </br><br/>
    _location_name:_ city name and country code of two characters <br/>
    _temperature:_ Temperature unit: Celsius <br/>
    _wind:_ description of the wild, wild speed and wild direction <br/>
    _cloudiness:_ description of the sky <br/>
    _pressure:_ Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa <br/>
    _humidity:_ Humidity, % <br/>
    _sunrise:_ sunrise time <br/>
    _sunset:_ sunset time <br/>
    _geo_coordinates:_ City geo location [longitude, latitude] <br/>
    _requested_time:_ Time of the request <br/>
    _forecast:_ {..} empy dict <br/><br/><br/>


**how to run  the code:**<br/>
    -- check the libraries: flask_caching, time, flask, requests <br/>
    -- on a python eviroment execute the command Flask run <br/>
    -- Use any browser to access http://127.0.0.1:5000/
