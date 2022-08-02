from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.match import Match
from app.models.question import Question
from app.models.user import User
import requests
import os
from dotenv import load_dotenv

load_dotenv()

users_bp = Blueprint("users_bp", __name__, url_prefix="/users")

def validate_user(user_id):
    try:
        user = int(user_id)
    except ValueError:
        response = {"msg": f"Invalid id: {user_id}"}
        abort(make_response(jsonify(response), 400))
    chosen_user = User.query.get(user_id)

    if chosen_user is None:
        response = {"msg": f"Could not find user with id #{user_id}"}
        abort(make_response(jsonify(response), 400))
    return chosen_user

