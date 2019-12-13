"""auth blueprint"""

from flask import Blueprint

from auth import register
from auth import login
from auth import logout

AUTH_BLUEPRINT = Blueprint('auth', __name__, url_prefix='/auth')

REGISTER_VIEW = register.RegisterAPI.as_view('register_api')
AUTH_BLUEPRINT.add_url_rule(
    'register',
    view_func=REGISTER_VIEW,
    methods=['POST']
)

LOGIN_VIEW = login.LoginAPI.as_view('login_api')
AUTH_BLUEPRINT.add_url_rule(
    'login',
    view_func=LOGIN_VIEW,
    methods=['POST']
)

LOGOUT_VIEW = logout.LogoutAPI.as_view('logout_api')
AUTH_BLUEPRINT.add_url_rule(
    'logout',
    view_func=LOGOUT_VIEW,
    methods=['GET']
)
