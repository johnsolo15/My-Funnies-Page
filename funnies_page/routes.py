from funnies_page import app
from flask import render_template, url_for, flash, redirect
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
    form = LoginForm()
    if form.validate_on_submit():
        #fake login
        flash('Logged in')
        flash('Login for {}'.format(form.email.data), 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #fake registration
        flash('Registered')
        flash('Registered {} with password {}'.format(form.email.data, form.password.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route('/comic/<name>')
def comic(name):
    #fake page
    return 'This is a page for ' + name