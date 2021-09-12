import requests
from app import app


# gets the current location of the user
def get_current_location():
    res = requests.get('https://extreme-ip-lookup.com/json/')
    country_code = res.json()["countryCode"].lower()

    return country_code

# gets the news depending on the resource specified
def get_news(resource, current_location):
    api_key = app.config["API_KEY"]
    base_url = app.config["BASE_URL"]
    res = requests.get(base_url.format(resource, 'us', api_key))
    print(base_url.format(resource, current_location, api_key))
    return res.json()
