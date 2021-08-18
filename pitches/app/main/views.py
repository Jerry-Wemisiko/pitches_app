from flask import render_template
from . import main
from ..models import User
from .. import  db

#Views
@main.route
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to Pitches'

    return render_template('index.html',title = title)
