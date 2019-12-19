"""appserver implement"""
import os

from flask import Flask
#extentions
from extensions import sqlalchemy
from extensions import bcrypt
#blueprints
from admin import admin_blueprint
from api import api_blueprint
from auth import auth_blueprint

BLUEPRINTS = (admin_blueprint.ADMIN_BLUEPRINT,
              auth_blueprint.AUTH_BLUEPRINT,
              api_blueprint.API_BLUEPRINT,
              )

def blueprints_fabrics(app, blueprints):
    """init blueprints"""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def extensions_fabrics(app):
    """init extensions"""
    sqlalchemy.db.init_app(app)
    bcrypt.bcrypt.init_app(app)
    #extensions.manager.init_app(app, falsk_sqlalchemy_db=db)

def create_app(config=None, app_name="todo-list", blueprints=None):
    """
    init flask
    loading configs
    init sub modules
    """
    app = Flask(
        app_name,
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
        template_folder='templates',
    )

    #app.config.from_object('project.config')
    app.config.from_pyfile('default.cfg', silent=False)
    if config:
        app.config.from_pyfile(config, silent=True)

    if blueprints is None:
        blueprints = BLUEPRINTS

    blueprints_fabrics(app, blueprints)
    extensions_fabrics(app)

    return app
