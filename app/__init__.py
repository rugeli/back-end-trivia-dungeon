from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

#holds configurations for the application 
def create_app():
        app = Flask(__name__)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #part of setting 
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
                "SQLALCHEMY_DATABASE_URI")


        from app.models.user import User
        from app.models.match import Match

        db.init_app(app)
        migrate.init_app(app, db)

        # Register Blueprints here
        from .user_routes import users_bp
        app.register_blueprint(users_bp)

        from .match_routes import matches_bp
        app.register_blueprint(matches_bp)

        CORS(app)
        return app