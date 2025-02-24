from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "google/gemini-2.0-flash-lite-preview-02-05:free"

class ModelBinder:

    def ask_model(self, prompt):
        response = requests.post(
            url="https://openrouter.ai/api/v1/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
                },
            data=json.dumps({
                "model": MODEL_NAME,
                "prompt": prompt
                }
            )
        )

        response_json = response.json()

        # Extract text from the first choice
        text = response_json["choices"][0]["text"] if "choices" in response_json and response_json["choices"] else "No response text found"

        # print(text)
        return text
    
    def ask_model_to_give_translation(self, text):
        prompt = (
            "You are a Japanese language translator.\n"
            "Provide a literal, accurate translation of the Japanese text to English.\n"
            "Only respond with the translation, no explanations.\n"
            f"Translate this Japanese text to English: '{text}'"
        )
        
        return self.ask_model(prompt)
    
    def ask_model_to_give_feedback(self, target_sentence, submission, translation):
        prompt = (
            "You are a Japanese language teacher grading student writing.\n"
            "Grade based on:\n"
            "- Accuracy of translation compared to target sentence\n"
            "- Grammar correctness\n"
            "- Writing style and naturalness\n\n"
            "Use S/A/B/C grading scale where:\n"
            "S: Perfect or near-perfect\n"
            "A: Very good with minor issues\n"
            "B: Good but needs improvement\n"
            "C: Significant issues to address\n\n"
            f"Grade this Japanese writing sample:\n"
            f"Target English sentence: {target_sentence}\n"
            f"Student's Japanese: {submission}\n"
            f"Literal translation: {translation}\n\n"
            "Provide your assessment in this format:\n"
            "Grade: [S/A/B/C]\n"
            "Feedback: [Your detailed feedback]\n"
        )            
        return self.ask_model(prompt)

if __name__ == "__main__":
    qg = ModelBinder()