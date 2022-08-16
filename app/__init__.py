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
        CORS(app)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #part of setting 
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
                "SQLALCHEMY_DATABASE_URI")
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
                "pool_pre_ping": True,
                "pool_recycle": 300,
                }
        



        from app.models.user import User
        from app.models.question import Question

        db.init_app(app)
        migrate.init_app(app, db)

        # Register Blueprints here
        from .user_routes import users_bp
        app.register_blueprint(users_bp)

        from .question_routes import questions_bp
        app.register_blueprint(questions_bp)

        return app