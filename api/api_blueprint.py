"""
blueprint for user's todo-list operations
"""
from flask import Blueprint

from api import items

API_BLUEPRINT = Blueprint('api', __name__, url_prefix='/')

ITEM_VIEW = items.ItemAPI.as_view('items')
API_BLUEPRINT.add_url_rule(
    'items',
    view_func=ITEM_VIEW,
    methods=['POST', 'PUT', 'GET', 'DELETE']
)
