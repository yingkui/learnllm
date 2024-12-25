from transformers import pipeline

def classify_tokens():
    # This can be used for NER, POS tagging, and more
    token_classifier = pipeline("token-classification", aggregation_strategy="simple")
    
    texts = [
        "Apple is looking at buying U.K. startup for $1 billion",
        "The Great Wall of China is over 13,000 miles long",
        "NASA's Perseverance rover landed on Mars in February 2021"
    ]
    
    print("\nToken Classification Examples:")
    for text in texts:
        results = token_classifier(text)
        print(f"\nText: {text}")
        print("Entities found:")
        for result in results:
            print(f"- {result['word']}: {result['entity_group']} "
                  f"(confidence: {result['score']:.3f})")

if __name__ == "__main__":
    classify_tokens()