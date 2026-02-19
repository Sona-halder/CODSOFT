import gradio as gr
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO

# Load pretrained BLIP model (ResNet + Transformer)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    """Extract image features (ResNet) → Generate caption (Transformer)"""
    # Process image
    inputs = processor(image, return_tensors="pt")
    
    # Generate caption
    out = model.generate(**inputs, max_length=50, num_beams=5)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

def create_interface():
    """Gradio UI for image upload + captioning"""
    interface = gr.Interface(
        fn=generate_caption,
        inputs=gr.Image(type="pil", label="Upload Image"),
        outputs=gr.Textbox(label="Generated Caption", lines=2),
        title="🖼️ Image Captioning AI",
        description="""**Computer Vision + NLP**: 
        ResNet extracts image features → Transformer generates natural captions.
        Works offline after first download.""",
        examples=[
            "https://images.unsplash.com/photo-1506905925346-21bda4d32df4",  # dog
            "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957",  # food
            "https://images.unsplash.com/photo-1441974231531-c6227db76b6e"   # city
        ]
    )
    return interface

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=True)
