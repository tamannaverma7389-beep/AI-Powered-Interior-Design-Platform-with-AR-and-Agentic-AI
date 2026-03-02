from transformers import pipeline

# simple zero-shot classifier
classifier = pipeline("zero-shot-classification")

def classify_furniture(image_url):
    labels = ["sofa", "chair", "table", "bed", "lamp"]

    result = classifier(
        "This is a piece of furniture",
        candidate_labels=labels
    )

    return result["labels"][0]