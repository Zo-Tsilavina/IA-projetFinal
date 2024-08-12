import requests
import json
from datetime import datetime
from weather import get_current_air_pollution, get_city_weather

import sys
import os

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def extract_3():
    # Utilisez une autre API ou méthode d'extraction pour cet extrait, si nécessaire
    cities = ["Tokyo", "New York", "Paris", "London", "Sydney"]
    for city in cities:
        air_pollution_data = get_current_air_pollution(city)
        weather_data = get_city_weather(city)
        
        with open(f'air_pollution/{city}_{datetime.now().strftime("%Y-%m-%d")}_data.json', 'w') as file:
            file.write(json.dumps({'air_pollution': air_pollution_data, 'weather': weather_data}, indent=4))
