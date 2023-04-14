from flask import Flask

from db import db
from views import query_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(query_blueprint)
    return app