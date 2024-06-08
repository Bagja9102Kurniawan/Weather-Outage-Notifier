import unittest
from weather_module import get_current_weather

class TestWeather(unittest.TestCase):

    def test_get_current_weather_success(self):
        """
        Test the get_current_weather function with a valid city name.
        """
        api_key = 'your_weatherbit_api_key'
        city = 'Tangerang'
        result = get_current_weather(api_key, city)
        self.assertIn('temperature', result)
        self.assertIn('description', result)

    def test_get_current_weather_invalid_city(self):
        """
        Test the get_current_weather function with an invalid city name.
        """
        api_key = 'your_weatherbit_api_key'
        city = 'InvalidCity'
        result = get_current_weather(api_key, city)
        self.assertEqual(result, 'Unknown error occurred')

if __name__ == '__main__':
    unittest.main()