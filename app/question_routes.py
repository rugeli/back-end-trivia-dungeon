from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.match import Match
from app.models.question import Question
import requests
import os
from dotenv import load_dotenv

load_dotenv()

questions_bp = Blueprint("questions_bp", __name__, url_prefix="/questions")

def validate_question(question_id):
    try:
        user = int(question_id)
    except ValueError:
        response = {"msg": f"Invalid id: {question_id}"}
        abort(make_response(jsonify(response), 400))
    chosen_question = Question.query.get(question_id)

    if chosen_question is None:
        response = {"msg": f"Could not find question with id #{question_id}"}
        abort(make_response(jsonify(response), 400))
    return chosen_question