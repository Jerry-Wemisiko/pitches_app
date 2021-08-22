from flask import render_template,abort,redirect,url_for,request
from . import main
from flask_login import login_required,current_user
from ..models import Comment, Pitch, User
from  .forms import UpdateProfile, formPitch
from .. import  db,photos
# import markdown2

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

@main.route('/create_new', methods = ["GET","POST"])
@login_required
def create_pitch():
    p_form = formPitch
    if p_form.validate_on_submit:
        title = p_form.title.data
        category = p_form.category.data
        info = p_form.info.data
        created_pitch = Pitch(title=title,category=category,info= info)
        created_pitch.save_pitch()
        return redirect(url_for(main.index))

    return render_template('new-pitch.html',form=p_form) 


@main.route('/comment/<int:id>')
@login_required
def comment(pitch_id):
    comment = Comment.query.get(pitch_id)
    if comment is None:
        abort(404)

    

@main.route('/user/<uname>',methods=["GET","POST"])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id=user.id)
    if user is None:
        abort(404)
    title = f'{user.username}'    
    return render_template('profile/userprofile.html',user=user,title=title,pitches=pitches)

@main.route('/user<uname>/update', methods = ["POST","GET"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)


@main.route('/user/<uname>/update/pic',methods = ["POST"])
@login_required
def update_pic(uname):
     user = User.query.filter_by(username = uname).first()
     if 'photo' in request.files:
         filename= photos.save(request.files['photo'])
         path = f'photos/{filename}'
         user.profile_pic_path = path
         db.session.commit()
     return redirect(url_for('main.profile',uname = uname))    
