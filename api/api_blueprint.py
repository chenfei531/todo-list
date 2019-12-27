"""
blueprint for user's todo-list operations
"""
from flask import Blueprint

from api import items

API_BLUEPRINT = Blueprint('api', __name__, url_prefix='/')

ITEM_VIEW = items.ItemAPI.as_view('items')

url = "user/<int:user_id>/items/"
API_BLUEPRINT.add_url_rule(
    url, view_func=ITEM_VIEW,
    methods=['GET'],
    defaults={"item_id": None}
)

API_BLUEPRINT.add_url_rule(
    url, view_func=ITEM_VIEW,
    methods=['POST']
)

API_BLUEPRINT.add_url_rule(
    '%s<int:item_id>' % url,
    view_func=ITEM_VIEW,
    methods=['PUT', 'GET', 'DELETE']
)
