import re
from typing import List, Optional
import ollama
import chromadb

class QuestionModel:
    def __init__(self, introduction: Optional[str], conversation: Optional[str], question: Optional[str], options: Optional[List[str]], situation: Optional[str]):
        self.introduction = introduction
        self.conversation = conversation
        self.question = question
        self.options = options
        self.situation = situation

class Questions:
    def __init__(self, section_name: str, question_model: QuestionModel):
        self.section_name = section_name
        self.question_model = question_model

def parse_file(file_path: str) -> List[Questions]:
    questions_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        sections = re.findall(r'<section_name\s*=\s*"(.*?)">(.*?)</section_name>', content, re.DOTALL)
        for section_name, section_content in sections:
            # Extract the numeric part of the section name
            section_number = re.search(r'\d+', section_name).group()

            questions = re.findall(r'<question>(.*?)</question>', section_content, re.DOTALL)
            for question_content in questions:
                introduction_match = re.search(r'Introduction:\s*(.*?)\n', question_content)
                introduction = introduction_match.group(1).strip() if introduction_match else None

                conversation_match = re.search(r'Conversation:\s*(.*?)\n', question_content)
                conversation = conversation_match.group(1).strip() if conversation_match else None

                question_match = re.search(r'Question:\s*(.*?)\n', question_content)
                question = question_match.group(1).strip() if question_match else None

                options_match = re.search(r'Options:\s*(.*?)\n', question_content)
                options = options_match.group(1).strip().split('\n') if options_match else None

                situation_match = re.search(r'Situation:\s*(.*?)\n', question_content)
                situation = situation_match.group(1).strip() if situation_match else None

                question_model = QuestionModel(introduction, conversation, question, options, situation)
                questions_list.append(Questions(section_number, question_model))

    return questions_list


class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name="docs")

    def add_documents(self, documents):
        for i, d in enumerate(documents):
            response = ollama.embed(model="mxbai-embed-large", input=d)
            embeddings = response["embeddings"]
            if not isinstance(embeddings, list) or not all(isinstance(e, list) for e in embeddings):
                raise ValueError("Embeddings must be a list of lists of floats.")
            self.collection.add(
                ids=[str(i)],
                embeddings=embeddings,
                documents=[d]
            )

    def query_document(self, input):
        response = ollama.embed(model="mxbai-embed-large", input=input)
        embeddings = response["embeddings"]
        if not isinstance(embeddings, list) or not all(isinstance(e, list) for e in embeddings):
            raise ValueError("Embeddings must be a list of lists of floats.")
        results = self.collection.query(
            query_embeddings=embeddings,
            n_results=1
        )
        data = results['documents'][0][0]
        return data

    def generate_response(self, input, data):
        output = ollama.generate(
            model="llama3.2:1b",
            prompt=f"Using this data: {data}. Respond to this prompt: {input}"
        )
        return output['response']

# Test case
if __name__ == "__main__":
    # documents = [
    #     "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
    #     "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
    #     "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
    #     "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
    #     "Llamas are vegetarians and have very efficient digestive systems",
    #     "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
    # ]

    # data_structurer = DataStructurer()
    # data_structurer.add_documents(documents)
    # input = "What animals are llamas related to?"
    # data = data_structurer.query_document(input)
    # response = data_structurer.generate_response(input, data)
    # print(response)

    # ****************************************** #
    # To test the parsing logic 
    # ****************************************** #
    # file_path = "backend/data/structured_data/sY7L5cfCWno.txt"
    # questions = parse_file(file_path)
    # for q in questions:
    #     print(f"Section: {q.section_name}")
    #     print(f"Introduction: {q.question_model.introduction}")
    #     print(f"Conversation: {q.question_model.conversation}")
    #     print(f"Question: {q.question_model.question}")
    #     print(f"Options: {q.question_model.options}")
    #     print(f"Situation: {q.question_model.situation}")
    #     print()
    # ****************************************** #

