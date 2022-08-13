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

def validate_user(netlify_id):
    # try:
    #     user = int(user_id)
    # except ValueError:
    #     response = {"msg": f"Invalid id: {user_id}"}
    #     abort(make_response(jsonify(response), 400))
    chosen_user = User.query.filter_by(netlify_id=netlify_id).first()

    if chosen_user is None:
        response = {"msg": f"Could not find user with id #{netlify_id}"}
        abort(make_response(jsonify(response), 400))
    # print("Chosen user", chosen_user)
    return chosen_user

@users_bp.route("", methods=["POST"])
def create_one_user():
    request_body = request.get_json()["postUser"]
    # print("request_body", request_body)
    if bool(User.query.filter_by(netlify_id=request_body["netlify_id"]).first()):
        return {"msg": "Welcome back!"}

    try:
        new_user = User(
            netlify_id=request_body["netlify_id"],
            name=request_body["name"],
            email=request_body["email"]
        )

        new_user.netlify_id = request_body["netlify_id"]
        new_user.name = request_body["name"]
        new_user.email = request_body["email"]
    
    except KeyError:
        return {
            "details": "Invalid data"
        }, 400

    db.session.add(new_user)
    db.session.commit()

    response = jsonify({"user": {"id": new_user.user_id, "netlify_id": new_user.netlify_id, "name": new_user.name, "email": new_user.email}})
    return response, 201

@users_bp.route("/<netlify_id>", methods=["GET"])
def get_one_user(netlify_id):
    chosen_user = validate_user(netlify_id)
    response = {"user": {
        "id": chosen_user.user_id,
        "netlify_id": chosen_user.netlify_id,
        "name": chosen_user.name,
        "email": chosen_user.email
    }}
    if chosen_user.highest_score is not None:
        response = {"user": {
        "id": chosen_user.user_id,
        "netlify_id": chosen_user.netlify_id,
        "name": chosen_user.name,
        "email": chosen_user.email,
        "high_score": chosen_user.highest_score,
        "personal_best_category": chosen_user.highest_category
    }}

    return jsonify(response),200

@users_bp.route("/<netlify_id>", methods=["PUT"])
def update_highest_score_and_category(netlify_id):
    chosen_user = validate_user(netlify_id)
    request_body = request.get_json()

    if not chosen_user.highest_score or request_body["highest_score"] > chosen_user.highest_score:
        try:
            chosen_user.highest_score = request_body["highest_score"]
            chosen_user.highest_category = request_body["highest_category"]

        except KeyError:
            return {
                "details": "Invalid data"
            } , 400
        
    db.session.commit()
    response = {"msg": f"High score of {chosen_user.highest_score}pts in category {chosen_user.highest_category}!"}
    return jsonify(response),200

@users_bp.route("/leaderboard", methods=["GET"])
def get_leader_board():
    response = User.query.filter(User.highest_score != None).order_by(User.highest_score.desc()).limit(10).all()
    # print (response)

    return jsonify(list(map(lambda x: ({
        "name": x.name,
        "email": x.email,
        "high_score": x.highest_score,
        "category": x.highest_category
    }), response))),200
    

@users_bp.route("/<netlify_id>", methods=["DELETE"])
def delete_one_user(netlify_id):
    chosen_user = validate_user(netlify_id)
    db.session.delete(chosen_user)
    db.session.commit()

    response = {"msg": f"delete user with id: {chosen_user.user_id}"}
    return jsonify(response), 200




