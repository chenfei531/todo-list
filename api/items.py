"""
add item api
"""
from flask.views import MethodView
from flask import request

from extensions import db_sqlite

from models import list_item
from auth import auth_util

class ItemAPI(MethodView):
    """
    items CRUD endpoints
    """
    def get(self):
        """query items"""
        ret = auth_util.auth_check(request)
        if isinstance(ret, str):
            return auth_util.make_json_response('fail', ret)

        id_int = int(ret['sub'])

        elements = list_item.Item.query.filter_by(owner_id=id_int).all()
        return auth_util.make_json_response('sucess', repr(elements))

    def post(self): # pylint: disable=no-self-use
        """add items"""
        ret = auth_util.auth_check(request)
        if isinstance(ret, str):
            return auth_util.make_json_response('fail', ret)
        #auth ok, do insert
        request_body = request.get_json()
        title_str = request_body.get('title')
        context_str = request_body.get('context')

        id_int = int(ret['sub'])

        ele = list_item.Item.query.filter_by(title=title_str,
                                             owner_id=id_int).first()
        if ele:
            return auth_util.make_json_response('fail', 'title already exists')
        new_item = list_item.Item(title=title_str,
                                  context=context_str,
                                  owner_id=id_int)
        db_sqlite.db.session.add(new_item)
        db_sqlite.db.session.commit()
        return auth_util.make_json_response('sucess', str(new_item) + ' added')

    def delete(self):
        """delete items"""
        ret = auth_util.auth_check(request)
        if isinstance(ret, str):
            return auth_util.make_json_response('fail', ret)
        request_body = request.get_json()
        title_str = request_body.get('title')

        id_int = int(ret['sub'])

        ele = list_item.Item.query.filter_by(title=title_str,
                                             owner_id=id_int).first()
        if not ele:
            return auth_util.make_json_response('fail', 'title not exists')
        db_sqlite.db.session.delete(ele)
        db_sqlite.db.session.commit()
        return auth_util.make_json_response('sucess', repr(ele) + 'deleted')

    def put(self):
        """update items"""
        ret = auth_util.auth_check(request)
        if isinstance(ret, str):
            return auth_util.make_json_response('fail', ret)
        request_body = request.get_json()
        title_str = request_body.get('title')
        context_str = request_body.get('context')

        id_int = int(ret['sub'])

        ele = list_item.Item.query.filter_by(title=title_str,
                                             owner_id=id_int).first()
        if ele:
            #when title already exists, update item
            ele.context = context_str
        else:
            #when title not exists, add item
            ele = list_item.Item(title=title_str,
                                 context=context_str, owner_id=id_int)
            db_sqlite.db.session.add(ele)
        db_sqlite.db.session.commit()
        return auth_util.make_json_response('sucess', str(ele) + ' updated')
