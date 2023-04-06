from flask_mysqldb import MySQL

import click
from flask import current_app, g


def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()
    cursor = db.connection.cursor()

    with current_app.open_resource('schema.sql') as f:
        cursor.execute(f.read().decode('utf8'))
        cursor.close()
        db.connection.commit()
        db.connection
    # MySQL.


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def get_db():
    if 'db' not in g:
        # print(current_app.config['MySQL_HOST'])
        g.db = MySQL(current_app)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    # if db is not None:
    #     MySQL().connection.
