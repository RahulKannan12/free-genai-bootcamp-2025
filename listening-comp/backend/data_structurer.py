# Use a pipeline as a high-level helper
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
## MODEL_NAME = "deepseek/deepseek-r1-distill-llama-70b:free"
MODEL_NAME = "google/gemini-2.0-flash-lite-preview-02-05:free"

class DataStructurer:
    def __init__(self, record: str):
        self.record = record

    def structure_data(self):
        data = self.load_data()
        # response = self.client.generate(
        #     input=data
        # )
        # return response['response']
        prompt = {
            1: """Extract questions from section 問題1 of this JLPT transcript where the answer can be determined solely from the conversation without needing visual aids.
            
            ONLY include questions that meet these criteria:
            - The answer can be determined purely from the spoken dialogue
            - No spatial/visual information is needed (like locations, layouts, or physical appearances)
            - No physical objects or visual choices need to be compared
            
            For example, INCLUDE questions about:
            - Times and dates
            - Numbers and quantities
            - Spoken choices or decisions
            - Clear verbal directions
            
            DO NOT include questions about:
            - Physical locations that need a map or diagram
            - Visual choices between objects
            - Spatial arrangements or layouts
            - Physical appearances of people or things

            Format each question exactly like this:

            <section_name = "問題1">
            <question>
            Introduction:
            [the situation setup in japanese]
            
            Conversation:
            [the dialogue in japanese]
            
            Question:
            [the question being asked in japanese]

            Options:
            1. [first option in japanese]
            2. [second option in japanese]
            3. [third option in japanese]
            4. [fourth option in japanese]
            </question>
            </section_name>

            Rules:
            - Only extract questions from the 問題1 section
            - Only include questions where answers can be determined from dialogue alone
            - Ignore any practice examples (marked with 例)
            - Do not translate any Japanese text
            - Do not include any section descriptions or other text
            - Output questions one after another with no extra text between them
            """,
            
            2: """Extract questions from section 問題2 of this JLPT transcript where the answer can be determined solely from the conversation without needing visual aids.
            
            ONLY include questions that meet these criteria:
            - The answer can be determined purely from the spoken dialogue
            - No spatial/visual information is needed (like locations, layouts, or physical appearances)
            - No physical objects or visual choices need to be compared
            
            For example, INCLUDE questions about:
            - Times and dates
            - Numbers and quantities
            - Spoken choices or decisions
            - Clear verbal directions
            
            DO NOT include questions about:
            - Physical locations that need a map or diagram
            - Visual choices between objects
            - Spatial arrangements or layouts
            - Physical appearances of people or things

            Format each question exactly like this:

            <section_name="問題2">
            <question>
            Introduction:
            [the situation setup in japanese]
            
            Conversation:
            [the dialogue in japanese]
            
            Question:
            [the question being asked in japanese]
            </question>
            </section_name>

            Rules:
            - Only extract questions from the 問題2 section
            - Only include questions where answers can be determined from dialogue alone
            - Ignore any practice examples (marked with 例)
            - Do not translate any Japanese text
            - Do not include any section descriptions or other text
            - Output questions one after another with no extra text between them
            """,
            
            3: """Extract all questions from section 問題3 of this JLPT transcript.
            Format each question exactly like this:

            <section_name="問題3">
            <question>
            Situation:
            [the situation in japanese where a phrase is needed]
            
            Question:
            何と言いますか
            </question>
            </section_name>

            Rules:
            - Only extract questions from the 問題3 section
            - Ignore any practice examples (marked with 例)
            - Do not translate any Japanese text
            - Do not include any section descriptions or other text
            - Output questions one after another with no extra text between them
            """
        }
        full_prompt = f"{prompt}\n\nNo need to add reasoning in the response\n\nHere's the transcript:\n{data}"
        # completion = self.client.completions.create(
        #     extra_headers={
        #         "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        #         "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        #         },
        #         extra_body={},
        #         model="deepseek/deepseek-r1-distill-llama-70b:free",
        #         prompt=full_prompt,
        #     )

        response = requests.post(
            url="https://openrouter.ai/api/v1/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
                },
            data=json.dumps({
                "model": MODEL_NAME,
                "prompt": full_prompt
                }
            )
        )

        # Parse response JSON
        response_json = response.json()

        # print(response_json)

        # Extract text from the first choice
        text = response_json["choices"][0]["text"] if "choices" in response_json and response_json["choices"] else "No response text found"

        # print(text)
        return text

    
    def load_data(self):
        data_folder = 'backend/data/transcripts/'
        file_path = os.path.join(data_folder, f"{self.record}.txt")
        # print(file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {self.record}.txt does not exist in the data folder.")
        
        with open(file_path, 'r') as file:
            data = file.read()
        
        return data
    
    def save_structured_data(self, structured_data : str):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'data', 'structured_data', f'{self.record}.txt')
            # print(file_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                file.write(structured_data)
            return True,self.record
        except Exception as e:
            return False,f"Error saving transcript: {e}"

# Test case
if __name__ == "__main__":
    sample_record = "sample_record"  # Replace with the actual record name
    data_structurer = DataStructurer('sY7L5cfCWno')
    structured_data = data_structurer.structure_data()
    data_structurer.save_structured_data(structured_data)
    print(structured_data)


