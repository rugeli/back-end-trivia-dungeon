from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.question import Question
from app.models.match import Match
import requests
import os
from dotenv import load_dotenv

load_dotenv()

matches_bp = Blueprint("matches_bp", __name__, url_prefix="/matches")

def validate_match(match_id):
    try:
        match = int(match_id)
    except ValueError:
        response = {"msg": f"Invalid id: {match_id}"}
        abort(make_response(jsonify(response), 400))
    chosen_match = Match.query.get(match_id)

    if chosen_match is None:
        response = {"msg": f"Could not find match with id #{match_id}"}
        abort(make_response(jsonify(response), 400))
    return chosen_match