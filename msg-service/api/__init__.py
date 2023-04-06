import os
import logging

from flask import Flask

from .chat import bp as chat_bp

from .db import init_app as db_init_app

# Create and configure the app.
#  - instance_relative_config=True tells the app that if there are configuration files relative to the instance folder, they should override the default configuration.
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    # A default secret key that should be overridden with a random value when deploying.
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'chat_gebeta.sqlite')
)

app.config.from_pyfile('config.py', silent=True)

db_init_app(app)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

logging.basicConfig(level=logging.DEBUG)

app.register_blueprint(chat_bp, url_prefix='/api')
