from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String)
    highest_score = db.Column(db.Integer)
    total_played = db.Column(db.Integer)