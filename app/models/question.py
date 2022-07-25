from app import db

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    correct_answer = db.Column(db.String)
    category = db.Column(db.String)