"""logout api"""

from flask.views import MethodView
from flask import request

from auth import auth_util

class LogoutAPI(MethodView): # pylint: disable=too-few-public-methods
    """
    logout view
    TODO: add token to blacklist after logout
          and schedule a task to clear old blacklisted tokens
    """
    def post(self): # pylint: disable=no-self-use
        """post callback"""
        #TODO: blacklist logout user

        return auth_util.make_json_response('sucess',
                                            ret['sub'] + ' logged out', 200)
