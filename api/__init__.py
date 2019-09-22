from api.search.controllers import search_blueprint as search
from api.user.controllers import user_blueprint as user
from api.slack.controllers import slack_blueprint as slack

from flask import Flask, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from config import BaseConfig
from config import configure_app

import os.path

app = Flask(__name__, static_folder='/static')

API_URL = '/static/swagger.json'
SWAGGER_URL = '/api/v1/docs'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Pave the Way Api"
    }
)

db = SQLAlchemy(app)

""" Corst settings will be here. We maybe use this endpoint later. """
cors = CORS(app, resources={
    r'/api/v1/*': {
        'origins': BaseConfig.ORIGINS
    }
})

configure_app(app)

app.url_map.strict_slashes = False

app.register_blueprint(search, url_prefix='/api/v1/search')
app.register_blueprint(user, url_prefix='/api/v1/user')
app.register_blueprint(slack, url_prefix='/api/v1/slack')
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
db.create_all()
