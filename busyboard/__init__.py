import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()


def create_app(config):
    # Set up app, database and login manager before importing models and controllers
    # Important for db_create script

    app = Flask(__name__)
    app.config.from_object(config)

    db.app = app
    db.init_app(app)

    from busyboard.models import User

    admin = Admin(app, name='BusyBoard', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session, endpoint='users'))

    @app.route('/')
    def main_route():
        users = User.query.all()
        return render_template('index.html', users=users)

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

