from transformers import pipeline

def translate_text():
    translator = pipeline('translation_en_to_fr')
    texts = [
        "AI is transforming the world.",
        "Hello, how are you today?",
        "Machine learning is fascinating."
    ]
    
    print("\nTranslation Examples (English to French):")
    for text in texts:
        translation = translator(text)
        print(f"\nEnglish: {text}")
        print(f"French: {translation[0]['translation_text']}")

if __name__ == "__main__":
    translate_text()