import requests
import json

import sys
import os

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def get_current_air_pollution(city):
    """
    Simule l'obtention des données de pollution de l'air pour une ville donnée.
    Vous devez remplacer cette fonction par l'appel à une vraie API.
    """
    # Remplacez ceci par un appel API réel pour obtenir les données de pollution de l'air
    # Exemple de réponse simulée
    air_pollution_data = {
        'Country': 'USA',
        'City': city,
        'AQI Value': 50,  # Valeur AQI simulée
        'AQI Category': 'Good',
        'CO AQI Value': 5,  # Valeur CO AQI simulée
        'CO AQI Category': 'Good',
        'Ozone AQI Value': 15,  # Valeur Ozone AQI simulée
        'Ozone AQI Category': 'Good',
        'NO2 AQI Value': 12,  # Valeur NO2 AQI simulée
        'NO2 AQI Category': 'Good',
        'PM2.5 AQI Value': 25,  # Valeur PM2.5 AQI simulée
        'PM2.5 AQI Category': 'Good',
        'newCountry': 'United States of America'
    }
    
    return air_pollution_data

def get_city_weather(city):
    """
    Obtenez les données météorologiques pour une ville donnée.
    Vous devez remplacer `YOUR_API_KEY` par votre clé API OpenWeatherMap.
    """
    api_key = '64c3b81d0e042e9ee938730c409c956d'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(api_url)
    data = response.json()
    
    weather_data = {
        'Country': 'USA',  # Remplacez par le pays réel si disponible dans l'API
        'City': city,
        'Temperature': data['main']['temp'],
        'Condition': data['weather'][0]['description'],
        'Humidity': data['main']['humidity'],
        'Wind Speed': data['wind']['speed']
    }
    
    return weather_data

def get_available_conditions():
    """
    Obtenez toutes les conditions météorologiques disponibles et les sauvegardez dans un fichier.
    """
    conditions = [
        'Clear',
        'Partly Cloudy',
        'Cloudy',
        'Rain',
        'Thunderstorm',
        'Snow'
    ]
    
    return conditions
