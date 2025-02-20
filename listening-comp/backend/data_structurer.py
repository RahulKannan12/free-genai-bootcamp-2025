import ollama
from ollama import chat
import os

class DataStructurer:
    def __init__(self, record: str):
        self.record = record
        # self.client = Client().create(
        #     model='my-assistant',
        #     from_='llama3.2:1b',
        #     system='You are an expert data cleanser, you are given a dataset and you need to structure in the provided format',
        #     stream=False,
        # )

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

            <question>
            Introduction:
            [the situation setup in japanese]
            
            Conversation:
            [the dialogue in japanese]
            
            Question:
            [the question being asked in japanese]
            </question>

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

            <question>
            Situation:
            [the situation in japanese where a phrase is needed]
            
            Question:
            何と言いますか
            </question>

            Rules:
            - Only extract questions from the 問題3 section
            - Ignore any practice examples (marked with 例)
            - Do not translate any Japanese text
            - Do not include any section descriptions or other text
            - Output questions one after another with no extra text between them
            """
        }
        full_prompt = f"{prompt}\n\nHere's the transcript:\n{data}"
        messages = [
            {
                'role': 'user',
                'content': full_prompt,
            },
        ]

        response = chat('llama3.2:3b-instruct-fp16', messages=messages)
        print(response['message']['content'])
    
    def load_data(self):
        data_folder = 'backend/data/transcripts/'
        file_path = os.path.join(data_folder, f"{self.record}.txt")
        print(file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {self.record}.txt does not exist in the data folder.")
        
        with open(file_path, 'r') as file:
            data = file.read()
        
        return data

# Test case
if __name__ == "__main__":
    sample_record = "sample_record"  # Replace with the actual record name
    data_structurer = DataStructurer('sY7L5cfCWno')
    structured_data = data_structurer.structure_data()
    print(structured_data)


