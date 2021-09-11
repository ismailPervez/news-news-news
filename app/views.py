from flask import render_template
from app import app

"""
Home page - the route that loads when the page first renders
"""
@app.route("/")
def index():
    return "Home Page!"