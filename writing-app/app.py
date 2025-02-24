import gradio as gr
import requests
import random
import logging
from model_binder import ModelBinder
from manga_ocr import MangaOcr
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize ModelBinder and MangaOCR
model = ModelBinder()
mocr = MangaOcr()

# Fetch words from API
API_URL = "http://localhost:5000/api/groups/:id/raw"
vocabulary = []

def fetch_vocabulary():
    global vocabulary
    try:
        logging.info("Fetching vocabulary from API...")
        response = requests.get(API_URL)
        response.raise_for_status()
        vocabulary = response.json()
        logging.info("Successfully fetched vocabulary.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching vocabulary: {e}")
    except Exception as e:
        logging.exception("Unexpected error occurred while fetching vocabulary.")

fetch_vocabulary()

# Function to get a random word
def get_random_word():
    try:
        if not vocabulary:
            logging.warning("Vocabulary is empty.")
            return "No words available", "", ""
        word = random.choice(vocabulary)
        logging.info(f"Selected random word: {word}")
        return word['Kanji'], word['reading'], word['english']
    except Exception as e:
        logging.exception("Error getting a random word.")
        return "Error", "", ""

# Function to process uploaded image and get transcription
def process_image(image):
    try:
        logging.info("Processing uploaded image for OCR...")
        img = Image.open(image.name)
        transcription = mocr(img)
        logging.info(f"OCR Transcription: {transcription}")
        
        translation = model.ask_model_to_give_translation(transcription)
        logging.info(f"Translation: {translation}")
        
        return transcription, translation
    except Exception as e:
        logging.exception("Error processing image.")
        return "Error processing image. Please try again.", ""

# Function to grade user input
def grade_submission(target_sentence, submission):
    try:
        logging.info("Grading user submission...")
        translation = model.ask_model_to_give_translation(submission)
        feedback = model.ask_model_to_give_feedback(target_sentence, submission, translation)
        logging.info(f"Feedback: {feedback}")
        
        grade, feedback_text = feedback.split("\n", 1) if "\n" in feedback else (feedback, "")
        return grade, feedback_text
    except Exception as e:
        logging.exception("Error grading submission.")
        return "Error", "Error grading submission. Please try again."

# UI components
def ui():
    with gr.Blocks() as demo:
        gr.Markdown("# Japanese Word Practice Playground")
        
        with gr.Row():
            get_word_btn = gr.Button("Get new word")
        
        kanji = gr.Textbox(label="Kanji", interactive=False)
        reading = gr.Textbox(label="Reading", interactive=False)
        english = gr.Textbox(label="English", interactive=False)
        gr.Markdown("**Please Practice**")
        
        get_word_btn.click(get_random_word, outputs=[kanji, reading, english])
        
        with gr.Row():
            file_upload = gr.File(label="Upload an image with Japanese text")
        gr.Markdown("**Upload an image containing Japanese text for transcription**")
        
        submit_btn = gr.Button("Submit", interactive=False)
        transcription_result = gr.Textbox(label="Transcription", interactive=False)
        translation_result = gr.Textbox(label="Translation", interactive=False)
        grade_result = gr.Textbox(label="Grade", interactive=False)
        feedback_result = gr.Textbox(label="Feedback", interactive=False)
        
        def enable_submit(file):
            logging.info("File uploaded successfully, enabling submit button.")
            return gr.update(interactive=True)
        
        file_upload.change(enable_submit, inputs=file_upload, outputs=submit_btn)
        
        submit_btn.click(process_image, inputs=file_upload, outputs=[transcription_result, translation_result])
        
        grade_btn = gr.Button("Get Grade")
        grade_btn.click(grade_submission, inputs=[english, transcription_result], outputs=[grade_result, feedback_result])
    
    logging.info("Launching Gradio UI...")
    demo.launch()

ui()
