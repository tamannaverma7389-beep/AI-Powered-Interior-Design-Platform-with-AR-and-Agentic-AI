from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))

    designs = db.relationship('Design', backref='user')
    bookings = db.relationship('Booking', backref='user')