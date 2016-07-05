from flask import Blueprint, request, render_template


users = Blueprint('users', __name__, template_folder='templates')


@users.route('/user/<int:pk>')
def user_detail(pk):
    print request
    print request.method  # ['GET', 'POST', ...]
    print request.args
    print request.headers
    return render_template(
        'users/detail.html',
        user_pk=pk,
    )
