import os

from flask import Flask
from flask_migrate import Migrate


from .models import db
from .seeds import seed, seed_commands
from .config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    app.cli.add_command(seed_commands)

    db.init_app(app)
    Migrate(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
