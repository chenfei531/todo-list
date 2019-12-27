"""auth utils"""

import datetime

from flask import make_response
from flask import jsonify

from extensions import jwt
from models import user

def init_auth_callbacks():
    @jwt.jwt.claims_verification_loader
    def my_claims_verification(user_claims):
        #nothing to do here for now
        return True

    @jwt.jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        return {
            'user_id' : identity,
        }


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
