from app import app 
from flask import render_template
from .request import get_sources

@app.errorhandler(404)
def not_found(error):
    all_sources = get_sources()
    all_sources = all_sources["sources"]
    
    return render_template('notfound.html', sources=all_sources)