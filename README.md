# Weather and Power Outage Notification Project

## Description
This project includes two main components:
1. Retrieve current weather data using the Weatherbit REST API.
2. Scrape power outage information from the RRI website and send automatic email notifications.

## Setup
Before running the scripts, ensure you have the required dependencies. You can install them using:
```sh
pip install -r requirements.txt
```

## Modules

### weather_module.py
This module contains functions to retrieve weather data from the Weatherbit API.

#### Functions:
- `get_current_weather(api_key, city)`: Retrieves current weather data for a specified city.
  - **Parameters:**
    - `api_key` (str): Your Weatherbit API key.
    - `city` (str): The name of the city to get weather data for.
  - **Returns:**
    - A dictionary containing city name, temperature, and weather description, or an error message.
  
#### How to Run
Replace `your_weatherbit_api_key` with your actual API key. Run the script to get the current weather data for Tangerang.

### outage_notifier.py
This module contains functions to check for power outages and send email notifications.

#### Functions:
- `get_outage_info(url)`: Scrapes power outage information from the specified URL.
  - **Parameters:**
    - `url` (str): The URL to scrape data from.
  - **Returns:**
    - A list of dictionaries containing title, description, and link for each power outage article.
  
- `send_email(subject, body, to_email)`: Sends an email with the specified subject and body to the given email address.
  - **Parameters:**
    - `subject` (str): The subject of the email.
    - `body` (str): The body of the email.
    - `to_email` (str): The recipient's email address.

#### How to Run
Replace `your_email@gmail.com` and `your_password` with your actual email credentials. Run the script to scrape power outage information and send an email notification.

## Unit Test
### test_weather_module.py
This module contains unit tests for `weather_module.py`.

#### Functions:
- `test_get_current_weather_success()`: Tests the `get_current_weather` function with a valid city name.
- `test_get_current_weather_invalid_city()`: Tests the `get_current_weather` function with an invalid city name.

#### How to Run
Replace `your_weatherbit_api_key` with your actual API key. Run the script to execute the unit tests.

#### Running Tests
To run the unit tests, use the following command from the directory containing `test_weather_module.py`:
```sh
python -m unittest discover -s . -p "test_*.py"
```
This will ensure that `unittest` properly discovers and runs your test file.