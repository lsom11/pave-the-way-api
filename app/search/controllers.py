# Import flask dependencies
from flask import Flask


# Set the route and accepted methods
@search.route('/search/', methods=['GET'])
def search():
    return 'this is where the json goes'