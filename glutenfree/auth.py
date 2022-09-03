from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from glutenfree import db

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template('login.html')


@auth.route("register")
def register():
    return render_template('register.html')


auth.route("/register", methods=['POST'])
def register_post():
    #  to validate and add user to database
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first()
    if user: 
        return redirect(url_for('auth.register'))
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route("/logout")
def logout():
    return 'Logout'