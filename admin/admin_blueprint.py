"""
only for test purposes in this project
"""

from flask import Blueprint

from extensions import sqlalchemy
from models import user
from models import list_item

ADMIN_BLUEPRINT = Blueprint('admin', __name__, url_prefix='/admin')

@ADMIN_BLUEPRINT.route('init')
def init():
    """init DB"""
    sqlalchemy.db.create_all()

    admin = user.User(username='123', password='123')
    sqlalchemy.db.session.add(admin)
    sqlalchemy.db.session.commit()
    new_item1 = list_item.Item(title='ABC', context='abc', owner_id=1)
    sqlalchemy.db.session.add(new_item1)
    sqlalchemy.db.session.commit()
    return 'inited'

@ADMIN_BLUEPRINT.route('clear_db')
def clear_db():
    """clear DB"""
    sqlalchemy.db.drop_all()
    return 'dropped'

@ADMIN_BLUEPRINT.route('add_user')
def add_user():
    """add user"""
    admin = user.User(username='admin', password='123')
    sqlalchemy.db.session.add(admin)
    sqlalchemy.db.session.commit()
    return 'admin_added'

@ADMIN_BLUEPRINT.route('show_user')
def show_user():
    """show all users"""
    return repr(user.User.query.all())

@ADMIN_BLUEPRINT.route('show_item')
def show_item():
    """show all items"""
    return repr(list_item.Item.query.all())
