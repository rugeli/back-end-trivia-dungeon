from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
mysql = MySQL()
load_dotenv()

#holds configurations for the application 
def create_app():
        app = Flask(__name__)
        CORS(app)
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #part of setting 
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
                "SQLALCHEMY_DATABASE_URI")

        app.config['MYSQL_DATABASE_USER'] = 'bb6b6b599e0afe4'
        app.config['MYSQL_DATABASE_PASSWORD'] = '0428810e'
        app.config['MYSQL_DATABASE_DB'] = 'heroku_7d82b560bf0c60d'
        app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-06.cleardb.net'
        mysql.init_app(app)


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