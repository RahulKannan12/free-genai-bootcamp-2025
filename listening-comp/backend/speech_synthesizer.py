from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

import torch
import soundfile as sf
import os

class SoundSynthesizer:
    def __init__(self):
        self.processor = None
        self.model = None
        self.vocoder = None
        self.speaker_embeddings = None

    def load_models(self):
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

        
        

    def generate_speech(self, text, fileName="speech", embeddings = None):
        # self.load_models()  # Load models only when needed
        print('hereeeee')

        inputs = self.processor(text=text, return_tensors="pt")
        speech = self.model.generate_speech(inputs["input_ids"], embeddings, vocoder=self.vocoder)

        output_dir = "frontend/static/audio"
        os.makedirs(output_dir, exist_ok=True)

        file = os.path.join(output_dir, f"{fileName}.wav")
        sf.write(file, speech.numpy(), samplerate=16000)
        return file

# Test case
if __name__ == "__main__":
    synthesizer = SoundSynthesizer()
    synthesizer.generate_speech("Hello, how are you?")
    print("Speech generated successfully")

