from . import db
from datetime import datetime

class Design(db.Model):
    __tablename__ = "designs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_image = db.Column(db.String(200))
    style_selected = db.Column(db.String(100))
    ai_output = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)