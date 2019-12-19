"""user Model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from extensions import sqlalchemy
from extensions import bcrypt

BASE = declarative_base()

class User(sqlalchemy.db.Model, BASE): # pylint: disable=too-few-public-methods
    """user model"""
    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    password = Column(String(64))

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.bcrypt.generate_password_hash(password).decode()

    def __repr__(self):
        return '<User %r>' % self.username
