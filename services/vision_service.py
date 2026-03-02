import cv2
import numpy as np

def analyze_room(image_path):
    image = cv2.imread(image_path)
    
    # Resize for faster processing
    image = cv2.resize(image, (600, 400))
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Edge detection
    edges = cv2.Canny(gray, 50, 150)
    
    # Extract dominant color
    pixels = image.reshape((-1, 3))
    avg_color = np.mean(pixels, axis=0)
    
    room_info = {
        "edges_detected": int(np.sum(edges > 0)),
        "dominant_color": avg_color.tolist()
    }
    
    return room_info