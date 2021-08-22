from flask import render_template,redirect,url_for,flash,request
from flask_login import login_required, logout_user,login_user
from ..models import Pitch, User
from .forms import RegistrationForm,LoginForm
from ..email import mail_message
from .. import db
from . import auth

@auth.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')
    title = "Pitches Login"    
    return render_template ('auth/login.html',login_form=login_form,title=title)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,username = form.username.data,password = form.password.data)
       
        db.session.add(user)
        db.session.commit()

        mail_message("We are Glad you are here","email/welcome_user",user.email,user = user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',registration_form= form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))