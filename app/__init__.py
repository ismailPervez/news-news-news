from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

# project configurations
app.config.from_pyfile('config.py')

from app import views
from app import errors