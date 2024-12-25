from transformers import pipeline

def recognize_entities():
    ner = pipeline('ner')
    texts = [
        "Microsoft CEO Satya Nadella announced new AI features in Seattle last week.",
        "Apple's Tim Cook visited Paris to open a new store near the Champs-Élysées."
    ]
    
    print("\nNamed Entity Recognition Examples:")
    for text in texts:
        entities = ner(text)
        print(f"\nText: {text}")
        print(f"Entities: {entities}")

if __name__ == "__main__":
    recognize_entities()
