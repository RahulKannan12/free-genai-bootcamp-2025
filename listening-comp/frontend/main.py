import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.youtube_transcriptor import get_transcript, save_transcript
from backend.data_structurer import DataStructurer
from backend.vector_store import VectorStore
from backend.question_generator import QuestionGenerator

# Page config
st.set_page_config(
    page_title="JLPT Listening Practice",
    page_icon="🎧",
    layout="wide"
)

def pull_transcript():
    st.subheader("Pull Transcript")
    youtube_url = st.text_input("YouTube URL")

    if 'transcript' not in st.session_state:
        st.session_state.transcript = ""

    if st.button("Pull Transcript"):
        st.session_state.transcript = get_transcript(youtube_url)
        st.write(st.session_state.transcript)

    if st.session_state.transcript:
        if st.button("Save Transcript"):
            success, result = save_transcript(youtube_url, st.session_state.transcript)
            message = "Saved Successfully" if success else "Error saving the file"
            if success:
                st.session_state.record = result
            st.write(message)

def structure_data():
    st.subheader("Structure Data")
    
    
    if('record') not in st.session_state:
        st.write("no transcript available for the session, load and save transcript first")
        return

    sd = DataStructurer(st.session_state.record)

    if st.session_state.record:
        if st.button("Structure Data"):
            print(st.session_state.record)
            result = sd.structure_data()
            st.write(result)
            st.session_state.structured_data = result

    if 'structured_data' not in st.session_state:
        st.session_state.structured_data = ""

    if st.session_state.structured_data:
        if st.button("Save Structured Data"):
            success, result = sd.save_structured_data(st.session_state.structured_data)
            message = "Saved Successfully" if success else "Error saving the file"
            st.write(message)

def rag_part():
    st.subheader("Indexing and Storing")
    if('record') not in st.session_state:
        st.write("no structured data is available for the session, structure the data first")
        return
    
    vs = VectorStore()

    if st.button("Index and Store Questions"):
        result = vs.index_questions_file(record = st.session_state.record)
        message = "Indexed and Saved Successfully" if result else "Error saving/indexing the file"
        st.write(message)

def interactive_learning():
    st.subheader("Interactive Learning")
    if 'question_generator' not in st.session_state:
        st.session_state.question_generator = QuestionGenerator()
    if 'current_question' not in st.session_state:
        st.session_state.current_question = None
    if 'current_practice_type' not in st.session_state:
        st.session_state.current_practice_type = None
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = None
    if 'current_question_options' not in st.session_state:
        st.session_state.current_question_options = None
    if 'current_question_answer' not in st.session_state:
        st.session_state.current_question_answer = None
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    
    practice_type = st.selectbox(
        "Select Practice Type",
        ["Dialogue Practice", "Phrase Matching"]
    )

    topics = {
        "Dialogue Practice": ["Daily Conversation", "Shopping", "Restaurant", "Travel", "School/Work"],
        "Phrase Matching": ["Announcements", "Instructions", "Weather Reports", "News Updates"]
    }

    topic = st.selectbox(
        "Select Topic",
        topics[practice_type]
    )

    if st.button("Generate Question"):
        section_num = 2 if practice_type == "Dialogue Practice" else 3
        new_question = st.session_state.question_generator.generate_questions(
            section_num, topic
        )
        st.session_state.current_question = new_question
        st.session_state.current_practice_type = practice_type
        st.session_state.current_topic = topic
        st.session_state.current_question_options = []
        st.session_state.current_question_answer = ""

    if st.session_state.current_question:
        st.write("### Current Question")
        question = st.session_state.current_question
        if question.get("Introduction"):
            st.write(f"**Introduction:** {question.get('Introduction')}")
        if question.get("Situation"):
            st.write(f"**Situation:** {question.get('Situation')}")
        if question.get("Conversation"):
            st.write(f"**Conversation:** {question.get('Conversation')}")
        if question.get("Question"):
            st.write(f"**Question:** {question.get('Question')}")
        if question.get("Options"):
            st.write("**Options:**")
            for option in question.get("Options", []):
                st.write(f"{option['number']}. {option['value']}")
                # st.session_state.current_question_options.append((option['value'], option['number']))
        if question.get("Answer"):
            st.session_state.current_question_answer = question.get("Answer")
        
        if st.session_state.current_question_answer and st.session_state.submitted:
                correct_answer = int(st.session_state.current_question_answer) - 1
                # options = st.session_state.current_question_options
                options = st.session_state.current_question.get("Options", [])
                selected_index = st.session_state.selected_answer - 1 if hasattr(st.session_state, 'selected_answer') else -1
                
                st.write("\n**Your Answer:**")
                for i, option in enumerate(options):
                    if i == correct_answer and i == selected_index:
                        st.success(f"{i+1}. {option} ✓ (Correct!)")
                    elif i == correct_answer:
                        st.success(f"{i+1}. {option} ✓ (This was the correct answer)")
                    elif i == selected_index:
                        st.error(f"{i+1}. {option} ✗ (Your answer)")
                    else:
                        st.write(f"{i+1}. {option}")

        else:
            options = st.session_state.current_question.get("Options", [])
            selected = st.radio(
                        "Choose your answer:",
                        options,
                        index=None,
                        format_func=lambda x: f"{x['value']}"
                    )
             # Submit answer button
            if selected and st.button("Submit Answer"):
                st.session_state.submitted = True
                selected_index = options.index(selected) + 1
                st.session_state.selected_answer = selected_index
                st.rerun()

def main():
    st.title("JLPT Listening Practice")

    # Sidebar menu
    st.sidebar.markdown("## Menu")
    menu = ["Pull Transcript", "Structure Data", "Indexing & Storing", "Interactive Learning"]
    choice = st.sidebar.radio("", menu)

    # Dictionary to map menu choices to functions
    menu_functions = {
        "Pull Transcript": pull_transcript,
        "Structure Data": structure_data,
        "Indexing & Storing": rag_part,
        "Interactive Learning": interactive_learning
    }

    # Call the function based on the menu choice
    if choice in menu_functions:
        menu_functions[choice]()

if __name__ == '__main__':
    main()
