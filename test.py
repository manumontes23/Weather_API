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

if __name__ == '__main__':
    unittest.main()
