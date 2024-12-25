from transformers import pipeline

def transcribe_speech():
    # You'll need to: pip install transformers[torch-speech]
    transcriber = pipeline("automatic-speech-recognition")
    
    # You can use audio file paths or URLs
    audio_paths = [
        "path/to/your/audio1.wav",
        "path/to/your/audio2.mp3"
    ]
    
    print("\nSpeech Recognition Examples:")
    for audio_path in audio_paths:
        try:
            result = transcriber(audio_path)
            print(f"\nAudio: {audio_path}")
            print(f"Transcription: {result['text']}")
        except Exception as e:
            print(f"Error processing {audio_path}: {str(e)}")

if __name__ == "__main__":
    transcribe_speech()