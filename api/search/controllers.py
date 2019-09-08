from flask import Blueprint, jsonify, request

search_blueprint = Blueprint('search', __name__)


@search_blueprint.route('/', methods=['GET'])

def search():
    return jsonify({"message": 'get off my server you bitches'})
