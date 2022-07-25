from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

#holds configurations for the application 
def create_app():
        app = Flask(__name__)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #kinda handy setting 
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
                "SQLALCHEMY_DATABASE_URI")

        db.init_app(app)
        migrate.init_app(app, db)

        return app