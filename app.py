import os
from flask import Flask
from flask_smorest import Api

from db import db
from dotenv import load_dotenv

import models

from resources.v1.recipes import blp as RecipesBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["API_TITLE"] = "Recipes API specification"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/recipes-api-specification"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(RecipesBlueprint)
    

    return app
