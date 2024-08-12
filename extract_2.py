import requests
import json
from datetime import datetime

import sys
import os

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def extract_2():
    cities = ["Tokyo", "New York", "Paris", "London", "Sydney"]
    api_key = "64c3b81d0e042e9ee938730c409c956d"  # Remplacez par votre clé API

    for city in cities:
        air_pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}"
        air_pollution_response = requests.get(air_pollution_url)
        air_pollution_data = air_pollution_response.json()
        
        with open(f'air_pollution/{city}_{datetime.now().strftime("%Y-%m-%d")}.json', 'w') as file:
            file.write(json.dumps(air_pollution_data, indent=4))
