import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-my-super-secret-key'
