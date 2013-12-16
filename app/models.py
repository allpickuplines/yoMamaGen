from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Jokes(Base):
    """A Joke Item."""
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key=True)
    joke = Column(Text, nullable=False)
    categories = Column(Text)

if __name__ == '__main__':
    from flask.ext.sqlalchemy import SQLAlchemy
    from app import app
    import re

    db = SQLAlchemy(app)
    db.Model = Base

    categories = db.session.query(
        Jokes.categories.distinct()).order_by(
        Jokes.categories).all()

    for category in categories:
        category = re.sub(r'(?i)([^\w])', '', str(category)[2:])
        print category
        jokes = db.session.query(Jokes).filter(
            Jokes.joke.contains(
                ' ' + category.lower() + ' ')).all()

        for joke in jokes:
            if category not in joke.categories:
                joke.categories += ',' + category
                db.session.commit()
