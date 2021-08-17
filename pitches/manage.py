from app import create_app,db
from app.models import User
from flask_script import Manager

app = create_app('production')
 

manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app =app, db = db)

if __name__ == '__main__':
    manager.run()