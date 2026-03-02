from . import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    furniture_name = db.Column(db.String(200))
    status = db.Column(db.String(50))
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)