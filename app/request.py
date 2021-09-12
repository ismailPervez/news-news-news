import requests
from app import app

def get_current_location():
    res = requests.get('https://extreme-ip-lookup.com/json/')
    country_code = res.json()["countryCode"].lower()

    return country_code

def get_latest_news(current_location):
    api_key = app.config["API_KEY"]
    base_url = app.config["BASE_URL"]
    res = requests.get(base_url.format(current_location, api_key))

    return res.json()
