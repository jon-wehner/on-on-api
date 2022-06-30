import os


class DevConfig:
    SQLAlchemy_DATABASE_URI = os.environ.get('DATABASE_URL')
