import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.youtube_transcriptor import get_transcript, save_transcript

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
            result = save_transcript(youtube_url, st.session_state.transcript)
            st.write(result)

def structure_data():
    st.subheader("Structure Data")
    st.write("This is the Structure Data screen. Add your code for Structure Data here.")

def rag_part():
    st.subheader("RAG Part")
    st.write("This is the RAG Part screen. Add your code for RAG Part here.")

def interactive_learning():
    st.subheader("Interactive Learning")
    st.write("This is the Interactive Learning screen. Add your code for Interactive Learning here.")

def main():
    st.title("JLPT Listening Practice")

    # Sidebar menu
    st.sidebar.markdown("## Menu")
    menu = ["Pull Transcript", "Structure Data", "RAG Part", "Interactive Learning"]
    choice = st.sidebar.radio("", menu)

    # Dictionary to map menu choices to functions
    menu_functions = {
        "Pull Transcript": pull_transcript,
        "Structure Data": structure_data,
        "RAG Part": rag_part,
        "Interactive Learning": interactive_learning
    }

    # Call the function based on the menu choice
    if choice in menu_functions:
        menu_functions[choice]()

if __name__ == '__main__':
    main()
