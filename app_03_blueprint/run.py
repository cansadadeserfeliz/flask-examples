from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('conf.config')

    from users.views import users
    app.register_blueprint(users, url_prefix='/users')

    return app
