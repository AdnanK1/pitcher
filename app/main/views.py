import email
from flask import render_template,redirect,url_for
from . import main
from .forms import RegisterForm
from ..models import User
from ..extensions import db

@main.route('/')
@main.route('/home')
def home_page():

    return render_template('home.html')

@main.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email=form.email.data,password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))

    return render_template('register.html', form=form)
