from dotenv import load_dotenv
import os
import requests
import json
from vector_store import VectorStore
import random
import re

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "google/gemini-2.0-flash-lite-preview-02-05:free"

class QuestionGenerator:
    def __init__(self):
        self.vector_store = VectorStore()
    
    def ask_model(self, prompt: str):
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
    
    def generate_questions(self, section_num, topic):
        similar_questions = self.vector_store.search_similar_questions(section_num, topic, n_results=3)

        if not similar_questions:
            print("No similar questions found")
        
        # Sort similar questions by similarity score in descending order
        similar_questions = sorted(similar_questions, key=lambda x: x['similarity_score'], reverse=True)
        
        context = "Here are some example JLPT training questions:\n\n"
        
        for idx, question in enumerate(similar_questions, start=1):
            context += f"Example - {idx}\n"
            context += f"Introduction: {question['introduction']}\n"
            if section_num == 2:
                context += f"Conversation: {question['conversation']}\n"
            
            if section_num == 3:
                if question['situation']:
                    context += f"   Situation: {question['situation']}\n"
            
            if question['question']:
                context += f"   Question: {question['question']}\n"
            if question['options']:
                context += f"   Options: {question['options']}\n"
            context += f"Answer: Option {random.choice([1, 2, 3, 4])}\n"
            context += "\n"
        

        # Create prompt for generating new question
        prompt = f"""Based on the following example JLPT listening questions, create a new question about {topic}.
        The question should follow the same format but be different from the examples.
        Make sure the question tests listening comprehension and has a clear correct answer.
        
        {context}
        
        Generate a new question following the exact same format as above. Include all components (Introduction/Situation, 
        Conversation/Question, and Options). Make sure the question is challenging but fair, and the options are plausible 
        but with only one clearly correct answer. Return ONLY the question without any additional text.
        
        Even though there might not be options in the provided example, always return with 4 options, Options are important

        New Question:
        """

        response = self.ask_model(prompt)

        ## Test Response for Section 3
        # response = """
        # Introduction: None
        # Situation: 電車の遅延に関するアナウンスが流れています。
        # Question: 何が原因で電車が遅れていますか。
        # Answer: Option 4

        # Option 1: 強風です。
        # Option 2: 事故です。
        # Option 3: 停電です。
        # Option 4: 線路の安全確認のためです。
        # """

        ## Test Response for Section 2
        # response = """
        # Introduction: 男の人は何を飲みますか

        # Conversation: いらっしゃいませ。ご注文はお決まりですか？ はい、私はコーヒーをください。 私はオレンジジュースをお願いします。 わかりました。 それでは、合計で二つで。すいません、私、ちょっと喉が渇いたので、もう一杯飲み物を注文してもいいですか？ もちろん！ 何になさいますか？ じゃあ、私はアイスティーにします。 ありがとうございます。

        # Answer: Option 3

        # Options:
        # 1. コーヒー
        # 2. オレンジジュース
        # 3. アイスティー
        # 4. もう一杯
        # """
        #print(response)

        # Parse the response
        response_lines = response.split('\n')
        response_obj = {
            "Introduction": None,
            "Conversation": None,
            "Answer": None,
            "Options": [],
            "Situation": None
        }
        
        for line in response_lines:
            check = line.strip()
            print(line)
            if check.startswith("Introduction:"):
                response_obj["Introduction"] = line.replace("Introduction: ", "").strip()
            elif check.startswith("Conversation:"):
                response_obj["Conversation"] = line.replace("Conversation: ", "").strip()
            elif check.startswith("Question:"):
                response_obj["Question"] = line.replace("Question: ", "").strip()
            elif check.startswith("Answer:"):
                response_obj["Answer"] = re.search(r"Option\s*(\d+)", line.replace("Answer: ", "").strip()).group(1)
            elif check.startswith("Options:"):
                continue
            elif check.startswith("1") or check.startswith("2.") or check.startswith("3.") or check.startswith("4.") or check.startswith("Option"):
                print('chi')
                if ":" in line:
                    parts = line.strip().split(": ")
                    number = int(parts[0].replace("Option", "").strip())
                    value = parts[1].strip()
                if "." in line:
                    parts = line.strip().split(". ")
                    number = int(parts[0])
                    value = parts[1].strip()  
                response_obj["Options"].append({"number" : number, "value": value })
            elif check.startswith("Situation:"):
                response_obj["Situation"] = line.replace("Situation: ", "").strip()
        
        # Ensure Situation is None if not available
        if not response_obj["Situation"]:
            response_obj["Situation"] = None

        print(json.dumps(response_obj, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    qg = QuestionGenerator()
    #qg.generate_questions(2, "restaurant")
    qg.generate_questions(3, "Announcements")