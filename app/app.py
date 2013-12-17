import random
import re
import os
from flask import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from models import Jokes, Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../yomama.db'

db = SQLAlchemy(app)
db.Model = Base

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/api/jokes/', defaults = {'category':None})
@app.route('/api/jokes/category/<category>/')
def get_jokes(category):
  if category:
    jokes = db.session.query(Jokes).filter(
      Jokes.categories.contains(category)).all()
  else:
    jokes = db.session.query(Jokes).all()
  output = []
  for joke in jokes:
    row = {}
    for field in Jokes.__table__.c:
      field = str(field).split('.')[1]
      row[field] = getattr(joke, field)
    output.append(row)
  return jsonify(jokes=output)

@app.route('/api/joke/', defaults = {'category':None})
@app.route('/api/joke/category/<category>/')
def get_random_joke(category):
  if category:
    rand = random.randrange(0, db.session.query(Jokes).filter(
      Jokes.categories.contains(category)).count())
    joke = db.session.query(Jokes.joke).filter(
      Jokes.categories.contains(category))[rand]
  else:
    rand = random.randrange(0, db.session.query(Jokes).count())
    joke = db.session.query(Jokes.joke)[rand]
  return jsonify(joke=joke)

@app.route('/api/categories/')
def get_categories():
  categories = (db.session.query(
    Jokes.categories.distinct()).order_by(
    Jokes.categories).all())
  output = []
  for category in categories:
    category = str(category).split(',')[0]
    category = re.sub(r'(?i)([^\w\s])', '', category[2:])
    if category not in output:
      output.append(category)
  return jsonify(categories=output)

if __name__ == '__main__':
    app.run(debug=True)
