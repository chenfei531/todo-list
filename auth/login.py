"""login api"""
from flask.views import MethodView
from flask import request
from flask import jsonify
from flask import make_response

from flask_jwt_extended import get_jti
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

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
                return auth_util.make_json_response('fail', 'user not exists',
                                                    404)
            #check password
            if not bcrypt.bcrypt.check_password_hash(
                    guest.password, password_str):
                return auth_util.make_json_response('fail', 'wrong password',
                                                    403)
            #generate token
            access_token = create_access_token(identity=guest.id)
            #refresh_token = create_refresh_token(identity=guest.id)

            access_jti = get_jti(encoded_token=access_token)
            #refresh_jti = get_jti(encoded_token=refresh_token)
            auth_util.revoked_store.set(access_jti, 'false', auth_util.ACCESS_EXPIRES * 1.2)
            #auth_util.revoked_store.set(refresh_jti, 'false', REFRESH_EXPIRES * 1.2)

            ret = {
                'access_token': access_token,
                #'refresh_token': refresh_token
            }
            return jsonify(ret), 201
        except Exception as e:
            return auth_util.make_json_response('fail', str(e), 500)
