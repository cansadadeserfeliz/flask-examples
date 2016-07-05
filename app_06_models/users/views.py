from flask import Blueprint, request, render_template

from .models import User, City

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/', defaults={'city_pk': None})
@users.route('/city/<int:city_pk>')
def user_list(city_pk):
    users = User.query
    city = None
    if city_pk:
        city = City.query.filter_by(id=city_pk).first_or_404()
        users = users.filter_by(city_id=city.id)
    return render_template(
        'users/list.html',
        users=users.all(),
        city=city,
    )



@users.route('/user/<int:pk>')
def user_detail(pk):
    user = User.query.filter_by(id=pk).first_or_404()
    return render_template(
        'users/detail.html',
        user=user,
    )
