"""todo-list item model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from extensions import sqlalchemy

BASE = declarative_base()
DB = sqlalchemy.db

class Item(DB.Model, BASE): # pylint: disable=too-few-public-methods
    """todo-list item model class"""
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    context = Column(String(512))
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = DB.relationship('User', backref=DB.backref('item', lazy='dynamic'))

    def __repr__(self):
        return '<Item %r, %r>' % (self.title, self.context)
