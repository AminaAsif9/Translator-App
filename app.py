import gradio as gr
from transformers import pipeline

# Load the translation model from Hugging Face
translator = pipeline("translation_en_to_ur", model="Helsinki-NLP/opus-mt-en-ur")

# Function to handle translation
def translate_to_urdu(text):
    return translator(text)[0]['translation_text']

# Gradio Interface setup
iface = gr.Interface(fn=translate_to_urdu, 
                     inputs="text", 
                     outputs="text", 
                     title="English to Urdu Translator", 
                     description="Enter English text to get its translation in Urdu.")

# Launch the Gradio interface
iface.launch()
