import requests
import json
from datetime import datetime
import sys
import os

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def extract_1():
    cities = ["Tokyo", "New York", "Paris", "London", "Sydney"]
    api_key = "64c3b81d0e042e9ee938730c409c956d"  # Remplacez par votre clé API

    for city in cities:
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        with open(f'air_pollution/{city}_{datetime.now().strftime("%Y-%m-%d")}.json', 'w') as file:
            file.write(json.dumps(weather_data, indent=4))
