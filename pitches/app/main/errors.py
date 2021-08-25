from flask import render_template
from . import main

@main.errorhandler(403)
def forbidden_access(error):
    '''
    Function to handles 403 error 
    '''
    return render_template('errors.html',error='page')
@main.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to handles 404 error 
    '''
    return render_template('errors.html',error='page')
@main.errorhandler(500)
def server_error(error):
    '''
    Function to handles 500 error 
    '''
    return render_template('errors.html',error='page')
