import os
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db
from models.user import User
from models.design import Design
from models.booking import Booking
from models.furniture import Furniture
from services.style_classifier import detect_style
from services.ai_recommendation import generate_recommendation
from services.vision_service import analyze_room
from services.booking_agent import confirm_booking

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
with app.app_context():
    db.create_all()

    # Insert default furniture if empty
    if not Furniture.query.first():
        db.session.add(Furniture(tag="Modern Sofa", style="modern", image_path="/static/furniture/sofa.jpg"))
        db.session.add(Furniture(tag="Luxury Bed", style="luxury", image_path="/static/furniture/bed.jpg"))
        db.session.add(Furniture(tag="Minimal Chair", style="minimalist", image_path="/static/furniture/chair.jpg"))
        db.session.commit()

# ===============================
# HOME
# ===============================
@app.route('/')
def home():
    return render_template("index.html")


# ===============================
# UPLOAD ROUTE
# ===============================
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        image = request.files['image']
        style = request.form['style']
        language = request.form['language']

        # Save image
        upload_folder = "static/uploads"
        os.makedirs(upload_folder, exist_ok=True)

        image_path = os.path.join(upload_folder, image.filename)
        image.save(image_path)

        # =====================
        # AI ANALYSIS
        # =====================
        analysis = analyze_room(image_path)

        style_detected = detect_style(image_path)

        ai_output = generate_recommendation(style_detected, analysis)

        # =====================
        # STYLE DETECTION LOGIC
        # =====================
        detected_style = "modern"  # default
        if "bed" in ai_output.lower():
            detected_style = "bedroom"
        elif "sofa" in ai_output.lower():
            detected_style = "livingroom"
        elif "kitchen" in ai_output.lower():
            detected_style = "kitchen"
        else:
            detected_style = "modern"

        # =====================
        # STATIC FURNITURE DATABASE
        # =====================
        furniture_db = {
            "modern": [
                {"tag": "Modern Sofa", "image_path": "/static/furniture/sofa.jpg"},
                {"tag": "Coffee Table", "image_path": "/static/furniture/table.jpg"},
                {"tag": "Wall Art", "image_path": "/static/furniture/wallart.jpg"},
            ],
            "bedroom": [
                {"tag": "King Size Bed", "image_path": "/static/furniture/bed.jpg"},
                {"tag": "Wardrobe", "image_path": "/static/furniture/wardrobe.jpg"},
            ],
            "livingroom": [
                {"tag": "Luxury Sofa", "image_path": "/static/furniture/sofa.jpg"},
                {"tag": "TV Unit", "image_path": "/static/furniture/tv.jpg"},
            ]
        }

        furniture_items = furniture_db.get(detected_style, furniture_db["modern"])
        furniture_items = Furniture.query.filter_by(style=detected_style).all()
        

        # =====================
        # SAVE DESIGN
        # =====================
        design = Design(
            user_id=1,
            room_image=image_path,
            style_selected=detected_style,
            ai_output=ai_output
        )

        db.session.add(design)
        db.session.commit()
        print("Furniture inserted successfully!")

        # =====================
        # RETURN RESULT PAGE
        # =====================
        return render_template(
            "recommendations.html",
            result=ai_output,
            image=image_path,
            furniture_items=furniture_items,
            language=language
        )

    return render_template("upload.html")


# ===============================
# BOOKING ROUTE
# ===============================
@app.route('/book/<item>/<language>')
def book(item, language):

    booking = Booking(
        user_id=1,
        furniture_name=item,
        status="Booked"
    )

    db.session.add(booking)
    db.session.commit()

    confirm_booking(f"{item} booked successfully", language)

    return redirect(url_for('dashboard'))


# ===============================
# DASHBOARD
# ===============================
@app.route('/dashboard')
def dashboard():

    designs = Design.query.all()
    bookings = Booking.query.all()

    return render_template(
        "dashboard.html",
        designs=designs,
        bookings=bookings
    )


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    app.run(debug=True)