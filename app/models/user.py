from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    highest_score = db.Column(db.Integer)
    highest_category = db.Column(db.Integer)
    matches = db.relationship("Match", back_populates="user", lazy=True)