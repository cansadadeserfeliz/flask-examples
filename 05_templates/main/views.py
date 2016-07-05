from flask import Blueprint, request, render_template


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template('main/index.html')
