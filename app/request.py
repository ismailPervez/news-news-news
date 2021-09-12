import requests

def get_current_location():
    res = requests.get('https://extreme-ip-lookup.com/json/')
    country_code = res.json()["countryCode"].lower()

    return country_code

    
