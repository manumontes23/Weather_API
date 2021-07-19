# Weather_API
endpoint get weather, flask


Get weather

parameters:
    city: name of the city <String>
    country: cod of the country, two caracters
response:
    location_name: city name and country code of two caracters 
    temperature: Temperature unit: Celsius
    wind: description of the wild, wild speed and wild direction
    cloudiness: description of the sky
    pressure: Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
    humidity: Humidity, %
    sunrise: sunrise time
    sunset: sunset time
    geo_coordinates: City geo location [longitude, latitude]
    requested_time: Time of the request
    forecast: {..} empy dict


how to run  the code:
    -- on a python eviroment execute the command Flask run
