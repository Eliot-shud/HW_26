from flask import Flask

import config
from db import db
from views import main_bp


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app