from flask import Blueprint

"""Blueprint for the application that houses defined URLs."""
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>Login</h1>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup')
def signup():
    return "<p>Sign up</p>"