"""
add item api
"""
from flask.views import MethodView
from flask import request

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_claims

from extensions import sqlalchemy_db

from models import list_item
from auth import auth_util

class ItemAPI(MethodView):
    """
    items CRUD endpoints
    """
    @jwt_required
    def get(self, user_id, item_id):
        """query items"""
        claims = get_jwt_claims()
        if claims['user_id'] != user_id:
            return auth_util.make_json_response('fail', 'cannot access', 401)
        if item_id is None:
            elements = list_item.Item.query.filter_by(owner_id=user_id).all()
        else:
            elements = list_item.Item.query.filter_by(owner_id=user_id,
                                                      id=item_id).all()
        return auth_util.make_json_response('sucess', repr(elements), 200)

    @jwt_required
    def post(self, user_id): # pylint: disable=no-self-use
        """add items"""
        claims = get_jwt_claims()
        if claims['user_id'] != user_id:
            return auth_util.make_json_response('fail', 'cannot access', 401)
        request_body = request.get_json()
        title_str = request_body.get('title')
        context_str = request_body.get('context')

        ele = list_item.Item.query.filter_by(title=title_str,
                                             owner_id=user_id).first()
        if ele:
            return auth_util.make_json_response('fail',
                                                'item already exists',
                                                409)
        new_item = list_item.Item(title=title_str,
                                  context=context_str,
                                  owner_id=user_id)
        sqlalchemy_db.db.session.add(new_item)
        sqlalchemy_db.db.session.commit()
        return auth_util.make_json_response('sucess', str(new_item.id) +
                                            ' added: ' + repr(new_item), 200)

    @jwt_required
    def delete(self, user_id, item_id):
        """delete items"""
        claims = get_jwt_claims()
        if claims['user_id'] != user_id:
            return auth_util.make_json_response('fail', 'cannot access', 401)
        ele = list_item.Item.query.filter_by(id=item_id,
                                             owner_id=user_id).first()
        if not ele:
            return auth_util.make_json_response('fail', 'item not exists', 404)
        sqlalchemy_db.db.session.delete(ele)
        sqlalchemy_db.db.session.commit()
        return auth_util.make_json_response('sucess',
                                            repr(ele) + 'deleted', 200)

    @jwt_required
    def put(self, user_id, item_id):
        """update items"""
        claims = get_jwt_claims()
        if claims['user_id'] != user_id:
            return auth_util.make_json_response('fail', 'cannot access', 401)
        request_body = request.get_json()
        title_str = request_body.get('title')
        context_str = request_body.get('context')

        ele = list_item.Item.query.filter_by(id=item_id,
                                             owner_id=user_id).first()
        if ele:
            #when title already exists, update item
            ele.title = title_str
            ele.context = context_str
        else:
            #when title not exists, add item
            ele = list_item.Item(title=title_str,
                                 context=context_str, owner_id=user_id)
            sqlalchemy_db.db.session.add(ele)
        sqlalchemy_db.db.session.commit()
        return auth_util.make_json_response('sucess', repr(ele) + ' updated',
                                            200)
