from flask import Blueprint, jsonify, request

search_blueprint = Blueprint('search', __name__)


@search_blueprint.route('/', methods=['GET'])

def search():
    name = request.form.get('name')
    return Response(), 200
