from flask import render_template
from . import main
from flask_login import login_required
from ..models import Pitch, User
from .. import  db

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to Pitches'
    pitches = Pitch.query.all()
    pickuplines = Pitch.query.filter_by(category = 'pickuplines').all()
    interviews = Pitch.query.filter_by(category = 'interviews').all()
    product = Pitch.query.filter_by(category = 'product').all()



    return render_template('index.html',title = title,piches=pitches,interviews=interviews,pickuplines=pickuplines,product=product)

