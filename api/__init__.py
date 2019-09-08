from api.search.controllers import search_blueprint as search
from api.user.controllers import user_blueprint as user
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy




from config import BaseConfig
from config import configure_app

app = Flask(__name__)

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
db.create_all()
