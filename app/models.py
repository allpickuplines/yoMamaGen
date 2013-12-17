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
        category = re.sub(r'(?i)([^\w\s])', '', str(category)[2:])
        print category
        if (category == 'Star Trek Wars Science Fiction Nerds'
            or category == 'Nerd Geek'
            or category == 'Math Related'):
            new_category = ['Geeky']
        elif category == 'Such Slut':
            new_category = ['Slut']
        elif category == 'Dumb Stupid':
            new_category = ['Stupid']
        elif category == 'Barack Obama':
            new_category = ['Political']
        elif category == 'Dirty Nasty Greasy':
            new_category = ['Dirty', 'Nasty', 'Greasy']
        else:
            new_category = [category]
        
        for cat in new_category:
            #Change name of initial category to new category
            jokes = db.session.query(Jokes).filter(
                Jokes.categories.contains(category)).all()
            for joke in jokes:
                joke.categories = cat
                db.session.commit()
            
            #Add categories to relevant jokes
            jokes = db.session.query(Jokes).filter(
                Jokes.joke.contains(
                    ' ' + cat.lower() + ' ')).all()

            for joke in jokes:
                if cat not in joke.categories:
                    joke.categories += ',' + cat
                    db.session.commit()
