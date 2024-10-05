from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

import re
from urllib.parse import urlparse, parse_qs, unquote


def get_address(latitude, longitude, timeout=10):
    geolocator = Nominatim(user_agent="geoapiExercises", timeout=timeout)
    
    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        
        if location:
            return location.raw.get('display_name', ''), location.raw.get('address', '')
        else:
            return None
    
    except GeocoderTimedOut:
        return None
    
    except GeocoderServiceError:
        return None


def extract_coordinates(url):
    decoded_url = unquote(url)
    
    # Проверка для 2GIS
    if "2gis" in decoded_url:
        match = re.search(r"geo/([\d.]+),([\d.]+)", decoded_url)
        if match:
            return float(match.group(2)), float(match.group(1))
        
        match = re.search(r"m=([\d.]+),([\d.]+)", decoded_url)
        if match:
            return float(match.group(2)), float(match.group(1))
    
    # Проверка для Google Maps
    elif "google" in decoded_url:
        match = re.search(r"/@([\d.]+),([\d.]+)", decoded_url)
        if match:
            return float(match.group(1)), float(match.group(2))
        
        query_params = parse_qs(urlparse(decoded_url).query)
        if "ll" in query_params:
            lat, lon = map(float, query_params["ll"][0].split(","))
            return lat, lon
    
    # Проверка для Яндекс.Карты
    elif "yandex" in decoded_url:
        query_params = parse_qs(urlparse(decoded_url).query)
        if "ll" in query_params:
            lon, lat = map(float, query_params["ll"][0].split(","))
            return lat, lon

    return 0.0, 0.0