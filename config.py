"""
Configuration of the website and database.
Copy this file to config.py and change the settings accordingly
"""
import os

basedir = os.getcwd()

# Flask settings, make sure to set the SECRET_KEY and turn DEBUG and TESTING to False for production
DEBUG = True
TESTING = True

SECRET_KEY = 'change me !'

# Database settings, database location and path to migration scripts
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'busyboard.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = DEBUG

UPLOADED_IMAGES_DEST = 'static/images'
UPLOADED_IMAGES_URL = '/static/images/'
