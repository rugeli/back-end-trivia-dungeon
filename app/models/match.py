from app import db

class Match(db.Model):
    match_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Integer)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=True)
    user = db.relationship("User", back_populates="matches")
