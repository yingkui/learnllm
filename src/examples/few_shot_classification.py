from transformers import pipeline

def few_shot_classify():
    classifier = pipeline("zero-shot-classification")
    
    # Example with few-shot learning approach
    examples = {
        "positive": [
            "This product is amazing!",
            "I love how this works"
        ],
        "negative": [
            "This is terrible quality",
            "I want my money back"
        ],
        "neutral": [
            "It's okay, nothing special",
            "Product arrived on time"
        ]
    }
    
    # New texts to classify
    texts_to_classify = [
        "This exceeded my expectations",
        "Not worth the price at all",
        "It does the job, I guess"
    ]
    
    print("\nFew-shot Classification Examples:")
    for text in texts_to_classify:
        result = classifier(text, list(examples.keys()))
        print(f"\nText: {text}")
        print(f"Classification: {result['labels'][0]} (confidence: {result['scores'][0]:.3f})")

if __name__ == "__main__":
    few_shot_classify()