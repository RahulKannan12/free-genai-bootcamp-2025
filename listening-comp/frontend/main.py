import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.youtube_transcriptor import get_transcript, save_transcript
from backend.data_structurer import DataStructurer
from backend.vector_store import VectorStore

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
    
    vs = VectorStore(record = st.session_state.record)

    if st.button("Index and Store Questions"):
        result = vs.index_questions_file()
        message = "Indexed and Saved Successfully" if result else "Error saving/indexing the file"
        st.write(message)

def interactive_learning():
    st.subheader("Interactive Learning")
    st.write("This is the Interactive Learning screen. Add your code for Interactive Learning here.")

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
