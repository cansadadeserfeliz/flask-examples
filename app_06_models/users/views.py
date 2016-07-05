from flask import Blueprint, request, render_template

from .models import User

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=User.query.all(),
    )



@users.route('/user/<int:pk>')
def user_detail(pk):
    user = User.query.filter_by(id=pk).first_or_404()
    return render_template(
        'users/detail.html',
        user=user,
    )
