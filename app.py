from flask import Flask
from flask_peewee.db import Database
from peewee import *

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


if __name__ == '__main__':
    Jokes.create_table(fail_silently=True)

    app.run()
