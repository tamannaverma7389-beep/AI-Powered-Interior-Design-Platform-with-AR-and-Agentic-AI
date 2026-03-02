from transformers import pipeline
import torch

# Load model once (important for performance)
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=0 if torch.cuda.is_available() else -1
)

def generate_recommendation(style, room_analysis):
    prompt = f"""
    You are an expert interior designer.
    Room Details: {room_analysis}
    Selected Style: {style}
    
    Suggest:
    - Furniture placement
    - Lighting ideas
    - Color palette
    - Decoration suggestions
    """

    response = generator(prompt, max_length=300, do_sample=True)
    return response[0]["generated_text"]