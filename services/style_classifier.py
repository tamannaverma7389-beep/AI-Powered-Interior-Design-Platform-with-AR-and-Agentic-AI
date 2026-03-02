from transformers import pipeline

classifier = pipeline(
    "zero-shot-image-classification",
    model="openai/clip-vit-base-patch32"
)

def detect_style(image_path):
    labels = ["modern interior", "traditional interior",
              "minimalist interior", "luxury interior"]

    result = classifier(image_path, candidate_labels=labels)
    return result[0]["label"].split()[0]