from flask import Flask
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'
mongo = PyMongo(app)


from funnies_page import routes, models
