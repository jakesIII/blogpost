from app import create_app, db
from flask_script import Manager, Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand
# import instances
app=create_app('development')
manager=Manager(app)
migrate=Migrate(app)
manager.add_command('db', MigrateCommand)
manager.add_command('serve', Server)

@manager.shell
def make_shell_context():
    return dict (app=app, db=db, User=User)

if __name__=='__main__':
    manager.run()
###you were working on the base html so you can extend it to auth templates broski then run the app
