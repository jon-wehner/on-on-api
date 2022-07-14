from flask import Blueprint
from app.models import User, db


auth_routes = Blueprint('auth', __name__)
