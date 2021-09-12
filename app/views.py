from flask import render_template
from app import app
from .request import get_news, get_sources

"""
Home page - the route that loads when the page first renders
"""
@app.route("/")
def index():
    all_sources = get_sources()
    all_sources = all_sources["sources"]
    news = get_news('top-headlines', 'bbc-news')
    if (news['status'] == 'ok'):
        news_articles = news["articles"]
    return render_template('home.html', articles=news_articles, sources=all_sources)

"""
Different news sources route
"""
@app.route("/<source>")
def news_source_articles(source):
    all_sources = get_sources()
    all_sources = all_sources["sources"]
    news = get_news('top-headlines', source)
    if (news['status'] == 'ok'):
        news_articles = news['articles']

    return render_template('source.html', articles=news_articles, sources=all_sources)        