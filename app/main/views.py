from flask import render_template,redirect,url_for
from . import main

@main.route('/')
@main.route('/home')
def home_page():

    return render_template('home.html')

