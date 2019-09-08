# Import flask dependencies
from flask import Blueprint, request, abort

# Import the database object from the main app module

from api.user.models import User, db


# Define the blueprint: 'auth', set its url prefix: app.url/auth
user_blueprint = Blueprint('user', __name__)

# Set the route and accepted methods
@user_blueprint.route('/<int:id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    return user


@user_blueprint.route("/create", methods=["POST"])
def create_user():
    user = User(
        email=request.form.get('email'),
        name=request.form.get('name'),
        password=request.form.get('password')
    )

    db.session.add(user)
    db.session.commit()

    return 'Successfully created user'
    
@user_blueprint.route("/<int:id>/edit", methods=['PUT'])
def edit_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    if not user:
        abort(404)

    user.name = request.form.get('name')
    user.email = request.form.get('email')

    db.session.commit()
    return 'Successfully edited user'


@user_blueprint.route("/<int:id>/delete", methods=["DELETE"])
def delete_post(user_id):
    user = User.query.filter_by(id=user_id).first()

    if not user:
        abort(404)

    db.session.delete(user)
    db.session.commit()

    return 'Successfully deleted'
