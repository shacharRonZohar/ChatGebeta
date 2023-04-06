import os

from flask import Flask

from .chat import bp as chat_bp
import logging

# def create_app(test_config=None):
# load_dotenv()
# Create and configure the app.
#  - instance_relative_config=True tells the app that if there are configuration files relative to the instance folder, they should override the default configuration.
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    # A default secret key that should be overridden with a random value when deploying.
    SECRET_KEY='dev',
    # port
)

# if test_config is None:
# Load the instance config, if it exists, when not testing.
app.config.from_pyfile('config.py', silent=True)
# else:
# Load the test config if passed in.
# app.config.from_mapping(test_config)

# Ensure the instance folder exists.
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

logging.basicConfig(level=logging.DEBUG)

app.register_blueprint(chat_bp, url_prefix='/api')
