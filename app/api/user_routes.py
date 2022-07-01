from flask import Blueprint


user_routes = Blueprint('users', __name__)


@user_routes.route('/helloworld')
def hello_world():
    return 'Hello World'
