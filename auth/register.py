"""register api"""

from flask import request
from flask.views import MethodView

from extensions import sqlalchemy_db
from models import user
from auth import auth_util

class RegisterAPI(MethodView): # pylint: disable=too-few-public-methods
    """register view"""
    def post(self): # pylint: disable=no-self-use
        """post callback"""
        post_data = request.get_json()
        if not post_data:
            return 'invalid request'
        username_str = post_data.get('username')
        password_str = post_data.get('password')
        if not username_str:
            return auth_util.make_json_response('fail', 'please enter username')
        if auth_util.user_exists(username_str):
            return auth_util.make_json_response('fail',
                                                'username already exists')
        if not password_str or not auth_util.password_check(password_str):
            return auth_util.make_json_response('fail', 'invalid password')

        new_user = user.User(username=username_str, password=password_str)
        sqlalchemy_db.db.session.add(new_user)
        sqlalchemy_db.db.session.commit()
        return auth_util.make_json_response('success',
                                            'user added, username: ' +
                                            username_str)
