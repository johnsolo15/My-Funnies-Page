from funnies_page import app
from flask import render_template, url_for, flash, redirect
from funnies_page.forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('comics_list.html')

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