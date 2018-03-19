from flask import render_template, url_for, flash, redirect, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from funnies_page import app, db
from funnies_page.models import User
from funnies_page.forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/home')
def index():
    #fake comic data
    comics = [
        {'name': 'Dilbert', 'url': '#'},
        {'name': 'Zits', 'url': '#'},
        {'name': 'Baby Blues', 'url': '#'},
        {'name': 'Sherman', 'url': '#'},
        {'name': 'Non Sequitur', 'url': '#'},
        {'name': 'WuMo', 'url': '#'},
        {'name': 'Broom Hilda', 'url': '#'},
        {'name': 'Peanuts', 'url': '#'},
        {'name': 'Frazz', 'url': '#'},
        {'name': 'Foxtrot', 'url': '#'}
    ]
    return render_template('comics_list.html', comics=comics)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Username or password is incorrect', 'danger')
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
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your are now registered! Please sign in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route('/comic/<name>')
def comic(name):
    #fake page
    return 'This is a page for ' + name

@app.route('/user/comics')
@login_required
def user_comics():
    return render_template('user_comics.html')
