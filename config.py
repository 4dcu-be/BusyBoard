"""
Configuration of the website and database.
Copy this file to config.py and change the settings accordingly
"""
import os

basedir = os.getcwd()

# Flask settings, make sure to set the SECRET_KEY and turn DEBUG and TESTING to False for production
DEBUG = False
TESTING = False

SECRET_KEY = 'change me !'

# Database settings, database location and path to migration scripts
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'busyboard.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = DEBUG

UPLOADED_IMAGES_DEST = 'busyboard/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
