import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    # Set up app, database and login manager before importing models and controllers
    # Important for db_create script

    app = Flask(__name__)
    app.config.from_object(config)

    db.app = app
    db.init_app(app)

    @app.route('/')
    def main_route():
        return 'hello world'

    @app.cli.command()
    def createdb():
        """
        function to create the initial database and migration information
        """
        SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

        if SQLALCHEMY_DATABASE_URI.startswith('sqlite:///'):
            path = os.path.dirname(os.path.realpath(SQLALCHEMY_DATABASE_URI.replace('sqlite:///', '')))
            if not os.path.exists(path):
                os.makedirs(path)

        db.create_all(app=app)

    return app

