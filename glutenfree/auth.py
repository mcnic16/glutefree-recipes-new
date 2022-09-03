from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from glutenfree.models import User
from glutenfree import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('cuisine'))


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    # validate and add user to database 
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first() 
    if user:
        flash('name already exists')
        return redirect(url_for('auth.register'))

    # create a new user with the form data
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'
