import os


class Config:
    SQLAlCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONs = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
