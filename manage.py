from flask.ext.script import Manager
from app.app import app

manager = Manager(app)
app.config['DEBUG'] = False

if __name__ == '__main__':
    manager.run()
