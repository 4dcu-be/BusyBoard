import os

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from busyboard.admin import UserAdminView, CustomIndexView
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

    admin = Admin(app, name='BusyBoard', template_mode='bootstrap3', index_view=CustomIndexView())
    admin.add_view(UserAdminView(User, db.session, endpoint='users'))

    @app.route('/')
    def main_route():
        users = User.query.all()
        return render_template('index.html', users=users)

    @app.route('/api/users')
    @app.route('/api/users/')
    def api_users():
        users = User.query.all()
        return jsonify(list([u.to_dict() for u in users]))

    @app.route('/api/users/<int:user_id>')
    def api_user(user_id: int):
        user = User.query.get(user_id)
        return jsonify(user.to_dict())

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

