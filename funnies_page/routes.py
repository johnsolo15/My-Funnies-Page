from flask import render_template, url_for, flash, redirect, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from funnies_page import app, mongo
from funnies_page.user import User
from funnies_page.forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/home')
def index():
    comics = mongo.db.comics.find().sort('name', 1).collation({'locale':'en', 'caseLevel': False})
    return render_template('comics_list.html', comics=comics)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user_doc = mongo.db.users.find_one({'email': form.email.data})
        if user_doc is None:
            flash('Email is incorrect', 'danger')
            return redirect(url_for('login'))
        user = User(user_doc)
        if not user.check_password(form.password.data):
            flash('Password is incorrect', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        mongo.db.users.insert_one(
            {
                'email': form.email.data,
                'password': User.hash_password(form.password.data)
            }
        )
        flash('Your are now registered! Please sign in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route('/comic/<name>')
def comic(name):
    name = name.replace('_', ' ')
    comic = mongo.db.comics.find_one({'name': name})
    return render_template('comic.html', title=comic['name'], comic=comic)

@app.route('/user/comics')
@login_required
def user_comics():
    return render_template('user_comics.html')
