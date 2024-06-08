import requests

def get_current_weather(api_key, city):
    base_url = "https://api.weatherbit.io/v2.0/current"
    params = {
        'city': city,
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if 'data' in data:
        weather = {
            'city': data['data'][0]['city_name'],
            'temperature': data['data'][0]['temp'],
            'description': data['data'][0]['weather']['description']
        }
        return weather
    else:
        return data.get('error', 'Unknown error occurred')

# Configuration
api_key = 'your_weatherbit_api_key'
city = 'Tangerang'
weather_data = get_current_weather(api_key, city)
print(weather_data)