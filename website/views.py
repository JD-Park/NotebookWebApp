from flask import Blueprint

"""Blueprint for the application that houses defined URLs."""
views = Blueprint('views', __name__)

"""Create the home route."""
@views.route('/')
def home():
    """This function will be called when you open the views route."""
    return "<h1>Test</h1>"