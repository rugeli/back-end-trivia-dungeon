from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.question import Card
from app.models.user import Board
import requests
import os
from dotenv import load_dotenv

load_dotenv()

question_bp = Blueprint("question_bp", __name__, url_prefix="/questions")
user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

