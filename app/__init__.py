# Import flask and template operators
from app.search.controllers import search as search
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return 'Not Found'


# Register blueprint(s)
app.register_blueprint(search)

