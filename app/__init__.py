import os

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS


from .models import db, User
from .seeds import seed, seed_commands
from .config import Config

login_manager = LoginManager()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    CORS(app)

    app.cli.add_command(seed_commands)

    db.init_app(app)
    Migrate(app, db)

    # Flask Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
