"""logout api"""

from flask.views import MethodView
from flask import request

from flask_jwt_extended import get_jti
from flask_jwt_extended import get_raw_jwt
from flask_jwt_extended import jwt_required

from auth import auth_util

class LogoutAPI(MethodView): # pylint: disable=too-few-public-methods
    """
    logout view
    """
    @jwt_required
    def delete(self): # pylint: disable=no-self-use
        """post callback"""
        jti = get_raw_jwt()['jti']
        auth_util.revoked_store.set(jti, 'true', auth_util.ACCESS_EXPIRES * 1.2)
        return auth_util.make_json_response('sucess', 'logged out', 200)
