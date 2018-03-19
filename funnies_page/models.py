from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from funnies_page import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}:{}>'.format(self.id, self.email)

class Comic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    source = db.Column(db.String(140))

    def __repr__(self):
        return '<Comic {}:{}>'.format(self.id, self.name)
 