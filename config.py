import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-my-super-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
