from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.question import Question
import requests
from dotenv import load_dotenv
from flask_cors import cross_origin

load_dotenv()

# local questions pool for later optimization, not used in trivia dungeon  

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
@cross_origin()
def get_all_categories():
    request_body = requests.get("https://opentdb.com/api_category.php").json()
    response = request_body["trivia_categories"]
    return jsonify(response), 200

@questions_bp.route("", methods=["POST"])
@cross_origin()
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


    response = {"msg": f"{len(questions)} questions have been successfully added"}
    return jsonify(response), 201


@questions_bp.route("/<question_id>", methods=["DELETE"])
@cross_origin()
def delete_one_question(question_id):
    chosen_question = validate_question(question_id)
    db.session.delete(chosen_question)
    db.session.commit()

    response = {"msg": f"delete question with id: {chosen_question.question_id}"}
    return jsonify(response), 200
    
