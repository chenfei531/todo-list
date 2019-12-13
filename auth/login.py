"""login api"""
from flask.views import MethodView
from flask import request
from flask import jsonify
from flask import make_response

from extensions import bcrypt

from models import user
from auth import auth_util

class LoginAPI(MethodView): # pylint: disable=too-few-public-methods
    """login view"""
    def post(self): # pylint: disable=no-self-use
        """post callback"""
        post_data = request.get_json()
        try:
            username_str = post_data.get('username')
            password_str = post_data.get('password')
            guest = user.User.query.filter_by(username=username_str).first()
            if not guest:
                #should redirect to register page
                return auth_util.make_json_response('fail', 'user not exists')
            #check password
            if not bcrypt.bcrypt.check_password_hash(
                    guest.password, password_str):
                return auth_util.make_json_response('fail', 'wrong password')
            #generate token
            auth_token = auth_util.encode_auth_token(str(guest.id))
            if not auth_token:
                return auth_util.make_json_response('fail', 'error gen token')
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(response_object))
        except Exception as e:
            return auth_util.make_json_response('fail', str(e))
