from . import db
from datetime import datetime

class Furniture(db.Model):
    __tablename__ = "furniture"

    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(200), nullable=False)
    tag = db.Column(db.String(100))
    style = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)