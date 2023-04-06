import logging
import os

from flask import Flask

from .model import bp as model_bp


def create_app(test_config=None):
    # Create and configure the app.
    #  - instance_relative_config=True tells the app that if there are configuration files relative to the instance folder, they should override the default configuration.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # A default secret key that should be overridden with a random value when deploying.
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'chat_gebeta.sqlite')
    )

    app.config.from_pyfile('config.py', silent=True)

    # logging.basicConfig(filename="chat-gebeta.log", level=logging.DEBUG)
    # Configure the logging module to log to a file & the standard output.
    logging.basicConfig(
        filename="./chat-gebeta.log",
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    if test_config is None:
        # Load the instance config, if it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in.
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(model_bp, url_prefix='/api/model')

    return app
