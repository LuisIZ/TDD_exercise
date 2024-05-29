# example.py
import requests
from fastapi import FastAPI

app = FastAPI()

def fetch_coordinates(city_name: str):
    '''
    Fetches the latitude and longitude of a given city name using OpenStreetMap's Nominatim service.
    '''
    api_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json"
    headers = {
        'User-Agent': 'Testing App'
    }
    response = requests.get(api_url, headers=headers)
    response_data = response.json()

    if not response_data:
        return None
    
    latitude = response_data[0]['lat']
    longitude = response_data[0]['lon']
    return float(latitude), float(longitude)

@app.get("/coordinates/")
def get_coordinates(city_name: str):
    return fetch_coordinates(city_name)