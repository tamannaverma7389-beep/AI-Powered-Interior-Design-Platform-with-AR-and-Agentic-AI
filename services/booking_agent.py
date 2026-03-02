from services.voice_service import generate_voice

def confirm_booking(item, language):
    text = f"Your {item} has been booked successfully."
    return generate_voice(text, language, "booking_confirmation.mp3")