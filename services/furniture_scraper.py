import requests
import os

UNSPLASH_ACCESS_KEY = "YOUR_API_KEY"

def fetch_furniture_images(query):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": 5,
        "client_id": UNSPLASH_ACCESS_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    os.makedirs("static/furniture", exist_ok=True)

    saved_images = []

    for i, photo in enumerate(data['results']):
        img_url = photo['urls']['regular']
        img_data = requests.get(img_url).content

        file_path = f"static/furniture/{query}_{i}.jpg"
        with open(file_path, "wb") as f:
            f.write(img_data)

        saved_images.append(file_path)

    return saved_images