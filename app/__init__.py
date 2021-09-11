from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# project configurations
app.config.from_pyfile('config.py')

from app import views