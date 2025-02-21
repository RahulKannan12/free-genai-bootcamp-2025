import re
from typing import List, Optional
import ollama
import chromadb
from chromadb.utils import embedding_functions
from typing import Dict, List, Optional
import json

class QuestionModel:
    def __init__(self, introduction: Optional[str], conversation: Optional[str], question: Optional[str], options: Optional[List[str]], situation: Optional[str]):
        self.introduction = introduction
        self.conversation = conversation
        self.question = question
        self.options = options
        self.situation = situation

    def to_dict(self):
        return {
            "introduction": self.introduction,
            "conversation": self.conversation,
            "question": self.question,
            "options": self.options,
            "situation": self.situation
        }

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

class LocalEmbeddingFunction(embedding_functions.EmbeddingFunction):
    def __init__(self, model_id="mxbai-embed-large"):
        self.model_id = model_id

    def __call__(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts using Bedrock"""
        embeddings = []
        for text in texts:
            try:
                response = ollama.embed(model=self.model_id, input=text)
                embedding = response["embeddings"]
                # Flatten the embeddings if they are nested
                if isinstance(embedding[0], list):
                    embedding = [item for sublist in embedding for item in sublist]
                embeddings.append(embedding)
            except Exception as e:
                print(f"Error generating embedding: {str(e)}")
                # Return a zero vector as fallback
                embeddings.append([0.0] * 1536)  # Titan model uses 1536 dimensions
        return embeddings

class VectorStore:
    def __init__(self, persist_directory: str = "backend/data/vectorstore"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.persist_directory = persist_directory
        self.embedding_fn = LocalEmbeddingFunction()
        self.collections = {
            "section2": self.client.get_or_create_collection(
                name="section2_questions",
                embedding_function=self.embedding_fn,
                metadata={"description": "JLPT listening comprehension questions - Section 2"}
            ),
            "section3": self.client.get_or_create_collection(
                name="section3_questions",
                embedding_function=self.embedding_fn,
                metadata={"description": "JLPT phrase matching questions - Section 3"}
            )
        }

    def index_questions_file(self, record):
        try:
            filename = "backend/data/structured_data/" + record + ".txt"
    
            # Parse questions from file
            questions = parse_file(filename)
            # print(questions)

            # Add to vector store
            if questions:
                self.add_questions(record, questions)
                # print(f"Indexed {len(questions)} questions from {filename}")
            
            return True
        except Exception as e:
            print(f"Error indexing questions: {str(e)}")
            return False

    def add_questions(self, record : str, questions: List[Questions]):
        """Add questions to the vector store"""
        ids = []
        documents = []
        metadatas = []
        
        for section in ['2', '3']:
            collection = self.collections[f"section{section}"]
            for idx, question in enumerate(questions):
                if question.section_name != section:
                    continue
                # Create a unique ID for each question
                question_id = f"{record}_{question.section_name}_{idx}"
                ids.append(question_id)
                
                # Store the full question structure as metadata
                metadatas.append({
                    "video_id": record,
                    "section": question.section_name,
                    "question_index": idx,
                    "full_structure": json.dumps(question.question_model.to_dict())
                })
                
                # Create a searchable document from the question content
                if question.section_name == '2':
                    document = f"""
                    Situation: {question.question_model.introduction}
                    Dialogue: {question.question_model.conversation}
                    Question: {question.question_model.question}
                    """
                else:  # section 3
                    document = f"""
                    Situation: {question.question_model.situation}
                    Question: {question.question_model.question}
                    """
                documents.append(document)
            
            # Add to collection
            # print("Adding to collection:")
            # print(f"IDs: {ids}")
            # print(f"Documents: {documents}")
            # print(f"Metadatas: {metadatas}")
            collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )

    def search_similar_questions(
        self, 
        section_num: int, 
        query: str, 
        n_results: int = 5
    ) -> List[Dict]:
        """Search for similar questions in the vector store"""
        if section_num not in [2, 3]:
            raise ValueError("Only sections 2 and 3 are currently supported")
        
        collection = self.collections[f"section{section_num}"]

        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        # Convert results to more usable format
        questions = []
        for idx, metadata in enumerate(results['metadatas'][0]):
            question_data = json.loads(metadata['full_structure'])
            question_data['similarity_score'] = results['distances'][0][idx]
            questions.append(question_data)
            
        return questions

    def write_output_to_file(self, output: List[Dict], file_path: str):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(output, file, ensure_ascii=False, indent=4)

# Test case
if __name__ == "__main__":
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
     # ****************************************** #
    # To test the vector store
    # ****************************************** #
    store = VectorStore()
    store.index_questions_file("sY7L5cfCWno")
    #similar = store.search_similar_questions(2, "誕生日について質問", n_results=1)
    similar = store.search_similar_questions(3, "Announcements", n_results=1)
    print("###SIMILAR###")
    print(similar)
    # Write the output to a 
    #output_file_path = "backend/data/output/similar_questions.json"
    #store.write_output_to_file(similar, output_file_path)
    #print(f"Output written to {output_file_path}")
    # ****************************************** #

