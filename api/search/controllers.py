from flask import Blueprint, jsonify, request, Response

search_blueprint = Blueprint('search', __name__)


@search_blueprint.route('/', methods=['GET'])
def search():
    name = request.args['name']
    return jsonify(
        name=name,
        status=200
    )
