from flask import render_template,redirect,url_for
from . import main
from .forms import RegisterForm

@main.route('/')
@main.route('/home')
def home_page():

    return render_template('home.html')

@main.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
