from flask import render_template,abort
from . import main
from flask_login import login_required
from ..models import Pitch, User
from  .forms import UpdateProfile
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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)