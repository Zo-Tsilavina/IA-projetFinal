import pandas as pd
import json
import os
import sys

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def transform_data():
    air_pollution_dir = 'air_pollution'
    files = [f for f in os.listdir(air_pollution_dir) if f.endswith('.json')]

    data = []
    for file in files:
        with open(f'{air_pollution_dir}/{file}', 'r') as f:
            file_data = json.load(f)
            city = file.split('_')[0]
            country = file_data.get('country', 'Unknown')
            aqi_value = file_data.get('aqi', 'N/A')
            aqi_category = file_data.get('aqi_category', 'N/A')
            co_aqi_value = file_data.get('co', 'N/A')
            co_aqi_category = file_data.get('co_category', 'N/A')
            ozone_aqi_value = file_data.get('o3', 'N/A')
            ozone_aqi_category = file_data.get('o3_category', 'N/A')
            no2_aqi_value = file_data.get('no2', 'N/A')
            no2_aqi_category = file_data.get('no2_category', 'N/A')
            pm25_aqi_value = file_data.get('pm2_5', 'N/A')
            pm25_aqi_category = file_data.get('pm2_5_category', 'N/A')

            data.append({
                'Country': country,
                'City': city,
                'AQI Value': aqi_value,
                'AQI Category': aqi_category,
                'CO AQI Value': co_aqi_value,
                'CO AQI Category': co_aqi_category,
                'Ozone AQI Value': ozone_aqi_value,
                'Ozone AQI Category': ozone_aqi_category,
                'NO2 AQI Value': no2_aqi_value,
                'NO2 AQI Category': no2_aqi_category,
                'PM2.5 AQI Value': pm25_aqi_value,
                'PM2.5 AQI Category': pm25_aqi_category,
                'newCountry': country
            })

    df = pd.DataFrame(data)
    df.to_csv('transformed_data.csv', index=False)
