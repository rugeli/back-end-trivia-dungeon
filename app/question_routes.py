from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.match import Match
from app.models.question import Question
import requests
import os
import json
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

@questions_bp.route("/categories", methods=["GET"])
def get_all_categories():
    request_body = requests.get("https://opentdb.com/api_category.php")
    response = request_body.json()
    return response, 200

@questions_bp.route("", methods=["POST"])
def create_one_question():
    # get questions 
    request_body = requests.get("https://opentdb.com/api.php?amount=10").json()
    questions = request_body["results"]

    # get categories
    category_request_body = requests.get("https://opentdb.com/api_category.php").json()
    categories = category_request_body["trivia_categories"]

    
    for question in questions:
        incorrect_answers = question["incorrect_answers"]
        new_question = Question(
            text=question["question"],
            correct_answer=question["correct_answer"],
            incorrect_answer_one=incorrect_answers[0]
        )

        if question["type"] == "multiple":
                new_question.incorrect_answer_two=incorrect_answers[1]
                new_question.incorrect_answer_three=incorrect_answers[2]

        for category in categories:
            if question["category"] == category["name"]:
                new_question.category=category["id"]
                

            
        db.session.add(new_question)
    db.session.commit()



    return jsonify(questions), 200
    
