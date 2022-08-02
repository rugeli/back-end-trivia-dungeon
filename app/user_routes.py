from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.match import Match
from app.models.question import Question
import requests
import os
from dotenv import load_dotenv

load_dotenv()

users_bp = Blueprint("users_bp", __name__, url_prefix="/users")

