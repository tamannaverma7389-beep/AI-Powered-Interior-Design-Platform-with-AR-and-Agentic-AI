from gtts import gTTS
import os

def generate_voice(text, language, filename):
    tts = gTTS(text=text, lang=language)
    path = os.path.join("static", filename)
    tts.save(path)
    return path