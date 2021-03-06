from flask import render_template,redirect,url_for, flash
from . import main
from .forms import RegisterForm, LoginForm,PitchForm,CommentForm
from ..models import User,Pitch,Comment
from ..extensions import db
from ..email import mail_message
from flask_login import login_user, logout_user

@main.route('/')
@main.route('/home')
def home_page():
    pitches = Pitch.query.all()
    comments = Comment.query.all()

    return render_template('home.html',pitches=pitches,comments=comments)

@main.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email=form.email.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        #mail_message("Welcome to Pitcher","email/welcome_user",user_to_create.email,user=user_to_create)

        return redirect(url_for('main.home_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You are loggied in as: {attempted_user.username}',category='success')
            return redirect(url_for('main.home_page'))
        else:
            flash('Username and password are not matching! Please try again', category='danger')

    return render_template('login.html', form=form)

@main.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!',category= 'info')
    return redirect(url_for('main.home_page'))

@main.route('/pitch',methods=['GET','POST'])
def pitch_page():
    form = PitchForm()
    if form.validate_on_submit():
        pitch_created = Pitch(pitch=form.pitch.data,category=form.category.data)
        db.session.add(pitch_created)
        db.session.commit()
        return redirect(url_for('main.home_page'))

    return render_template('pitch.html', form=form)

@main.route('/comment',methods=['GET','POST'])
def comment_page():
    form = CommentForm()
    if form.validate_on_submit():
        comment_created = Comment(name=form.name.data,comment=form.comment.data)
        db.session.add(comment_created)
        db.session.commit()
        return redirect(url_for('main.home_page'))

    return render_template('comment.html', form = form)