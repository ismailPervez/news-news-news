from flask import render_template
from app import app
from .request import get_current_location

"""
Home page - the route that loads when the page first renders
"""
@app.route("/")
def index():
    country_code = get_current_location()
    return render_template('home.html', location=country_code)

"""

"""