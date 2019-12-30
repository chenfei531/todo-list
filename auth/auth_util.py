"""auth utils"""

import datetime

import redis

from flask import make_response
from flask import jsonify

from extensions import jwt
from models import user

ACCESS_EXPIRES = datetime.timedelta(minutes=15)
revoked_store = redis.StrictRedis(host='redisdb', port=6379, db=0,
                                  decode_responses=True)

def init_auth_callbacks():
    @jwt.jwt.claims_verification_loader
    def my_claims_verification(user_claims):
        """jwt verification, nothing to do here for now"""
        return True

    @jwt.jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        """add claims to access_token"""
        return {
            'user_id' : identity,
        }

    @jwt.jwt.token_in_blacklist_loader
    def check_if_token_is_revoked(decrypted_token):
        """check if user is logout"""
        jti = decrypted_token['jti']
        entry = revoked_store.get(jti)
        if entry is None:
            return True
        return entry == 'true'

def user_exists(buf):
    """check if user exists"""
    if None is user.User.query.filter_by(username=buf).first():
        return False
    return True

def make_json_response(status, msg, ret=200):
    """generate common json response"""
    response_object = {
        'status' : status,
        'message' : msg
    }
    return make_response(jsonify(response_object)), ret
