from flask import render_template,redirect,url_for
from . import main

@main.route('/')
@main.route('/home')
def index():

    return render_template('index.html')