from app import db

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(900))
    correct_answer = db.Column(db.String(100))
    incorrect_answer_one = db.Column(db.String(100))
    incorrect_answer_two = db.Column(db.String(100))
    incorrect_answer_three = db.Column(db.String(100), nullable=True)
    category = db.Column(db.Integer)
