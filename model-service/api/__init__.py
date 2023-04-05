import os

from flask import Flask

from .model import bp as model_bp
# import logging
# from dotenv import load_dotenv


def create_app(config=None, import_name=__name__):
    # Create and configure the app.
    #  - instance_relative_config=True tells the app that if there are configuration files relative to the instance folder, they should override the default configuration.
    app = Flask(import_name, instance_relative_config=True)
    app.config.from_mapping(
        # A default secret key that should be overridden with a random value when deploying.
        SECRET_KEY='dev',
        # port
    )

    if config is None:
        # Load the instance config, if it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in.
        app.config.from_mapping(config)

    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # logging.basicConfig(level=logging.DEBUG)
    app.register_blueprint(model_bp, url_prefix='/api/model')

    return app
