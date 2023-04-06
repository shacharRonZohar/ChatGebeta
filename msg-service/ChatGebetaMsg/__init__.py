import os
import logging

from flask import Flask, g

from .blueprints.chat import bp as chat_bp
from .blueprints.auth import bp as auth_bp

from .db import init_app


def create_app(test_config=None):
    print('Creating app...')
    # Create and configure the app.
    #  - instance_relative_config=True tells the app that if there are configuration files relative to the instance folder, they should override the default configuration.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # A default secret key that should be overridden with a random value when deploying.
        SECRET_KEY='dev',
        DEBUG=False,
        # MySQl_URL='mysql://root:ERshOmOfFNltDJcYF7BK@containers-us-west-73.railway.app:5829/railway',
        # DATABASE=os.path.join(app.instance_path, 'chat_gebeta.sqlite')
        MYSQL_HOST='containers-us-west-73.railway.app',
        MYSQL_USER='root',
        MYSQL_PASSWORD='ERshOmOfFNltDJcYF7BK',
        MYSQL_DB='railway',
        MYSQL_PORT=5829,
        MYSQL_CURSORCLASS="DictCursor"
    )

    # app.config['MySQL_HOST'] = 'containers-us-west-73.railway.app'
    # app.config['My']

    # g.db = MySQL(app)

    app.config.from_pyfile('config.py', silent=True)

    init_app(app)

    logging.basicConfig(
        filename="./chat-gebeta.log",
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    )
    logging.getLogger().addHandler(logging.StreamHandler())

    init_app(app)

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

    app.register_blueprint(chat_bp, url_prefix='/chat')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
