import unittest
import app


class WeatherTest(unittest.TestCase):

    def test_get_weather(self):
        response = app.get_info_openweather('medellin', 'co')
        self.assertEqual(response.status_code, 200)

    def test_formating(self):
        response = {'coord': {'lon': -75.558, 'lat': 6.3373}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}],
                    'base': 'stations', 'main': {'temp': 292.92, 'feels_like': 293.51, 'temp_min': 292.8, 'temp_max': 294.59, 'pressure': 1017, 'humidity': 98, 'sea_level': 1017, 'grnd_level': 862},
                    'visibility': 10000, 'wind': {'speed': 1.1, 'deg': 72, 'gust': 1.35}, 'clouds': {'all': 87}, 'dt': 1626571952,
                    'sys': {'type': 2, 'id': 2002201, 'country': 'CO', 'sunrise': 1626519286, 'sunset': 1626564097},
                    'timezone': -18000, 'id': 3688928, 'name': 'Bello', 'cod': 200}
        formating_response = {'location_nme': 'Bello, CO', 'temperature': '20.0 °C', 'wind': {'speed': 1.1, 'deg': 72, 'gust': 1.35},
                              'cloudiness': 'overcast clouds', 'pressure': '1017hpa', 'humidity': '98%',
                              'sunrise': '10:54', 'sunset': '23:21', 'geo_coordinates': [-75.558, 6.3373], 'requested_time': '2021-07-18 01:32:32',
                              'forecast': {}}
        self.assertEqual(formating_response, app.formating(response))

    #Test Wind Decription
    
    def test_calm_wind(self):
        self.assertEqual(app.wind_description(0.3),"calm")

    def test_calm_light_air(self):
        self.assertEqual(app.wind_description(1.3),"Light air")
    
    def test_Light_breeze(self):
        self.assertEqual(app.wind_description(2.5),"Light breeze")

    def test_Gentle_breeze(self):
        self.assertEqual(app.wind_description(5),"Gentle breeze")
    
    def test_Moderate_breeze(self):
        self.assertEqual(app.wind_description(7.5),"Moderate breeze")

    def test_Fresh_breeze(self):
        self.assertEqual(app.wind_description(8.8),"Fresh breeze")

    def test_Strong_breeze(self):
        self.assertEqual(app.wind_description(12),"Strong breeze")

    def test_High_wind(self):
        self.assertEqual(app.wind_description(14.5),"High wind")
    
    def test_gale(self):
        self.assertEqual(app.wind_description(20),"Gale")

    def test_strong_gale(self):
        self.assertEqual(app.wind_description(20),"Strong gale")

    def test_storm(self):
        self.assertEqual(app.wind_description(26.7),"Storm")
    
    def test_violent_storm(self):
        self.assertEqual(app.wind_description(31.3),"Violent Storm")
    
    def test_hurricane(self):
        self.assertEqual(app.wind_description(34),"Hurricane")

if __name__ == '__main__':
    unittest.main()
