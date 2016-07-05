# -*- coding: utf-8 -*-
from inspect import getmembers

from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('conf.config')

    from main.views import main
    app.register_blueprint(main)

    from users.views import users
    app.register_blueprint(users, url_prefix='/users')

    @app.context_processor
    def constants_processor():
        from main import constants
        context = {}
        for name, item in getmembers(constants):
            context[name] = item
        return context

    return app

    return app
