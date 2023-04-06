import os

from flask import Flask

from .model import bp as model_bp

# Create and configure the app.
#  - instance_relative_config=True tells the app that if there are configuration files relative to the instance folder, they should override the default configuration.
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    # A default secret key that should be overridden with a random value when deploying.
    SECRET_KEY='dev',
)

app.config.from_pyfile('config.py', silent=True)


try:
    os.makedirs(app.instance_path)
except OSError:
    pass
app.register_blueprint(model_bp, url_prefix='/api/model')
