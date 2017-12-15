from flask import Flask, render_template
from jobplus.config import configs
# from simpledu.models import db, Course, User
from flask_migrate import Migrate
from flask_login import LoginManager



def register_blueprints(app):
    from .handlers import front , job , company , user , admin
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(user)
    app.register_blueprint(admin)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    #register_extensions(app)
    register_blueprints(app)

    return app