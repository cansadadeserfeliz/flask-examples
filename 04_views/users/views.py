from flask import Blueprint


users = Blueprint('users', __name__, template_folder='templates')


@users.route("/")
def hello():
    return "Hello Worlds!"


@users.route('/user/<name>')
def user_profile(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@users.route('/user/<int:pk>')
def user_detail(pk):
    return '<h1>Hello, user #{}!</h1>'.format(pk)


@users.route('/user/<int:pk>/create', methods=('POST',))
def user_create(pk):
    pass
