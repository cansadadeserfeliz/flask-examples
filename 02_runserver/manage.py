from flask import Flask
from flask.ext.script import Manager

from run import create_app

app = create_app()
manager = Manager(app)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    manager.run()