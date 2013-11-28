from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Jokes(Base):
    """A Joke Item."""
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key=True)
    joke = Column(Text, nullable=False)
    categories = Column(Text)
