# Initial Project Prompt

You're a expert python developer, Help me generating as single page application using python library Gradio with the below specs

1. When the app initialized , fetch from the GET localhost:5000/api/groups/:id/raw, this will return a collection of words in a json structure. 
The structure of the words object is 
{
    'Kanji' : '',
    'reading' : '',
    'english' : ''
}
It will have japanese words with their english translation. We need to store this collection of words in memory in the name "vocabulary"
2. Add a Title to the page as "Japanese Word Practice Playground", it should be big with greater font size, and other heading related styles
3. The app should have a button named "Get new word", on clicking this button we should display a randon word from "vocabulary", and the system should display Kanji, reading, english , and a instruction "Please Practise" in the UI, all in seperate Textbox
4. Next, coming to upload component, the user can upload an Image, the upload component should have the instructions clearly
5. Finally, the UI should have "Submit" button, which is read-only on initialization, and should be made clickable when the file is uploaded successfully
6. Atlast, we have a seperate component called "Result", the result should show the following information, the transcription output from the image uploaded and final Grade provided by the system

# Mock server Prompt

Great, help me generate a simple mock server in python which can handle and pass a set of dummy data for our endpoint "http://localhost:5000/api/groups/:id/raw"

