import requests
from app import app

api_key = app.config["API_KEY"]

# get all news sources
def get_sources():
    res = requests.get(f"https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}")
    return res.json()

# gets the news depending on the resource specified
def get_news(resource, news_source):
    base_url = app.config["BASE_URL"]
    res = requests.get(base_url.format(resource, news_source, api_key))

    return res.json()
