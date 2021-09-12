from flask import render_template
from app import app
from .request import get_news

"""
Home page - the route that loads when the page first renders
"""
@app.route("/")
def index():
    news_source = 'bbc-news'
    news = get_news('top-headlines', news_source)
    if (news['status'] == 'ok'):
        news_articles = news["articles"]
    return render_template('home.html', articles=news_articles)

"""

"""