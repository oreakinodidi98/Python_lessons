import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Conditions***\n')

    city = input(f'\nEnter the city name: ')
    
    API_KEY = os.getenv('API_KEY')
    
    request_url= f'https://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&q={city}&units=metric'

    print(request_url)

    weather_data = requests.get(request_url).json()

    print(weather_data)

    pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}.')
    print(f'\nThe Temp is {weather_data["name"]["temp"]}.')
    print(f'\n{weather_data["weather"][0]["description"].capitalize()} , Feels like {weather_data["name"]["feels_like"]} degrees.')


if __name__ == '__main__':
    get_current_weather()