from transformers import pipeline
import soundfile as sf

def text_to_speech():
    # You'll need to: pip install transformers[torch-speech] soundfile
    synthesizer = pipeline("text-to-speech", model="microsoft/speecht5_tts")
    
    texts = [
        "Hello! This is a test of text to speech synthesis.",
        "Artificial Intelligence is transforming the world!"
    ]
    
    print("\nText-to-Speech Examples:")
    for i, text in enumerate(texts):
        print(f"\nGenerating speech for: {text}")
        speech = synthesizer(text)
        
        # Save the audio file
        output_path = f"speech_output_{i}.wav"
        sf.write(output_path, speech["audio"], speech["sampling_rate"])
        print(f"Audio saved to: {output_path}")

if __name__ == "__main__":
    text_to_speech()