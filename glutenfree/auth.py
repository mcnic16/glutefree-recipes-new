from flask import Blueprint
from glutenfree import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/register')
def register():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'