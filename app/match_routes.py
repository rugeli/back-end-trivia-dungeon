from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.question import Question
import requests
import os
from dotenv import load_dotenv

load_dotenv()

matches_bp = Blueprint("matches_bp", __name__, url_prefix="/matches")