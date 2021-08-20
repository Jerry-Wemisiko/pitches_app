from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, SelectField, TextAreaField, SubmitField

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Care to tell us more about you",validators = [Required()])
    submit = SubmitField('Post')

    
class formPitch(FlaskForm):
    title = StringField('Title',validators =[Required()])
    category = SelectField()
