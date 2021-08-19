from typing_extensions import Required
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, TextAreaField

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Care to tell us more about you",validators = [Required()])
    submit = SubmitField('Post')

    
