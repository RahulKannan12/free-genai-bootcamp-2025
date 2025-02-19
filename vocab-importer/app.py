import gradio as gr
from ollama import generate

def greet(category):
    prompt = f"""Give me a list of japanese vocabulary language based on the thematic category `{category}` for the generation of japanese language vocabulary.
Include all the vocabulary based on the thematic category provided.
Generate at least 10 vocabulary words.
It has to create a structured json output exactly like the below
[
  {{
    "kanji": "払う",
    "romaji": "harau",
    "english": "to pay",
    "parts": [
      {{ "kanji": "払", "romaji": ["ha","ra"] }},
      {{ "kanji": "う", "romaji": ["u"] }}
    ]
  }},
  {{
    "kanji": "行く",
    "romaji": "iku",
    "english": "to go",
    "parts": [
      {{ "kanji": "行", "romaji": ["i"] }},
      {{ "kanji": "く", "romaji": ["ku"] }}
    ]
  }},
  {{
    "kanji": "運動する",
    "romaji": "undousuru",
    "english": "to exercise",
    "parts": [
      {{ "kanji": "運", "romaji": ["un"] }},
      {{ "kanji": "動", "romaji": ["do","u"] }},
      {{ "kanji": "す", "romaji": ["su"] }},
      {{ "kanji": "る", "romaji": ["ru"] }}
    ]
  }},
  {{
    "kanji": "起きる",
    "romaji": "okiru",
    "english": "to wake up",
    "parts": [
      {{ "kanji": "起", "romaji": ["o"] }},
      {{ "kanji": "き", "romaji": ["ki"] }},
      {{ "kanji": "る", "romaji": ["ru"] }}
    ]
  }},
  {{
    "kanji": "買い物する",
    "romaji": "kaimonosuru",
    "english": "to shop",
    "parts": [
      {{ "kanji": "買", "romaji": ["ka"] }},
      {{ "kanji": "い", "romaji": ["i"] }},
      {{ "kanji": "物", "romaji": ["mo", "no"] }},
      {{ "kanji": "す", "romaji": ["su"] }},
      {{ "kanji": "る", "romaji": ["ru"] }}
    ]
  }},
  {{
    "kanji": "帰る",
    "romaji": "kaeru",
    "english": "to return",
    "parts": [
      {{ "kanji": "帰", "romaji": ["ka", "e"] }},
      {{ "kanji": "る", "romaji": ["ru"] }}
    ]
  }},
  {{
    "kanji": "書く",
    "romaji": "kaku",
    "english": "to write",
    "parts": [
      {{ "kanji": "書", "romaji": ["ka"] }},
      {{ "kanji": "く", "romaji": ["ku"] }}
    ]
  }},
  {{
    "kanji": "観光する",
    "romaji": "kankousuru",
    "english": "to sightsee",
    "parts": [
      {{ "kanji": "観", "romaji": ["kan"] }},
      {{ "kanji": "光", "romaji": ["kou"] }},
      {{ "kanji": "す", "romaji": ["su"] }},
      {{ "kanji": "る", "romaji": ["ru"] }}
    ]
  }},
  {{
    "kanji": "聞く",
    "romaji": "kiku",
    "english": "to listen",
    "parts": [
      {{ "kanji": "聞", "romaji": ["ki"] }},
      {{ "kanji": "く", "romaji": ["ku"] }}
    ]
  }},
  {{
    "kanji": "来る",
    "romaji": "kuru",
    "english": "to come",
    "parts": [
      {{ "kanji": "来", "romaji": ["ku"] }},
      {{ "kanji": "る", "romaji": ["ru"] }}
    ]
  }}
]
don't add any extra texts in the result, just add the json alone
"""
    print(prompt)
    response = generate('llama3.2:1b', prompt)
    print(response['response'])
    return response['response']
    

demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
    allow_flagging="never",
    title="Vocabulary Importer",
    description="Generate japanese language vocabulary based on the thematic category provided"
)

demo.launch()