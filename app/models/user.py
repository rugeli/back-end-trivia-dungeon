from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    netlify_id = db.Column(db.String(200))
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), nullable=False)
    highest_score = db.Column(db.Integer)
    highest_category = db.Column(db.Integer)