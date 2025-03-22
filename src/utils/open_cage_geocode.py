from dotenv import load_dotenv
import os
from opencage.geocoder import OpenCageGeocode

load_dotenv()

API_KEY = os.getenv('OPEN_CAGE_API')

geocoder = OpenCageGeocode(API_KEY)

def get_coordinates(address):
    results = geocoder.geocode(address)
    if results and 'geometry' in results[0]:
        geometry = results[0]['geometry']
        if 'lat' in geometry and 'lng' in geometry:
            return geometry['lat'], geometry['lng']

    raise ValueError(f"Neplatná odpoveď na adresu: {address}")


coordinates = get_coordinates("Kartepe, Kocaeli, Turkey")
print("Zemepisná šírka a dĺžka:", coordinates)