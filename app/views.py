from flask import render_template
from app import app
from .request import get_current_location, get_news

"""
Home page - the route that loads when the page first renders
"""
@app.route("/")
def index():
    country_code = get_current_location()
    news = get_news('top-headlines', country_code)
    if (news['status'] == 'ok'):
        news_articles = news["articles"]
    return render_template('home.html', articles=news_articles)

"""

"""