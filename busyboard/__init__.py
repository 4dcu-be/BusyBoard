import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, form
from flask_admin.menu import MenuLink
from busyboard.admin import UserAdminView
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class

db = SQLAlchemy()

images = UploadSet('images', IMAGES)


def create_app(config):
    # Set up app, database and login manager before importing models and controllers
    # Important for db_create script

    app = Flask(__name__)
    app.config.from_object(config)

    db.app = app
    db.init_app(app)

    configure_uploads(app, (images))
    patch_request_class(app, 16 * 1024 * 1024)

    from busyboard.models import User

    admin = Admin(app, name='BusyBoard', template_mode='bootstrap3')
    admin.add_view(UserAdminView(User, db.session, endpoint='users'))
    admin.add_link(MenuLink('Back', '/', 'back'))

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

