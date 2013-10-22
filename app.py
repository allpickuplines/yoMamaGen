from flask import Flask, render_template
from peewee import *
from flask_peewee.db import Database
from flask_peewee.rest import RestAPI

# configure our database
DATABASE = {
    'name': 'yomama.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper
db = Database(app)


class Jokes(db.Model):
    joke = TextField()
    categories = TextField()

api = RestAPI(app)
api.register(Jokes)
api.setup()

@app.route('/')
def homepage():
	return render_template('index.html')

if __name__ == '__main__':
    Jokes.create_table(fail_silently=True)

    app.run()
