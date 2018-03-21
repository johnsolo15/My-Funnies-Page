from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from bson import ObjectId
from funnies_page import mongo, login

@login.user_loader
def load_user(user_id):
    user_doc = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user_doc is None:
        return None
    return User(user_doc)

class User(UserMixin):
    def __init__(self, user_doc):
        self.id = str(user_doc['_id'])
        self.email = user_doc['email']
        self.password_hash = user_doc['password']

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
 