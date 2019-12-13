"""auth utils"""

import datetime

import jwt

from flask import current_app
from flask import make_response
from flask import jsonify

from models import user

def encode_auth_token(key):
    """generate auth token"""
    try:
        payload = {
            'exp': datetime.datetime.utcnow() +
                   datetime.timedelta(days=0, seconds=600),
            'iat': datetime.datetime.utcnow(),
            'sub': key
        }
        return jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e

def auth_check(req):
    """check if user is authorized"""
    auth_header = req.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        return 'Invalid header'

    try:
        payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
    except jwt.ExpiredSignatureError:
        return 'Signature expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'
    #TODO: check if token is expired via blacklist
    return payload

def user_exists(buf):
    """check if user exists"""
    if None is user.User.query.filter_by(username=buf).first():
        return False
    return True

def password_check(buf):
    """
    password strength check
    TODO: add constraints
    """
    return buf

def make_json_response(status, msg, ret=200):
    """generate common json response"""
    response_object = {
        'status' : status,
        'message' : msg
    }
    return make_response(jsonify(response_object)), ret
