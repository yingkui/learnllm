from transformers import pipeline

def zero_shot_classify():
    classifier = pipeline("zero-shot-classification")
    
    # Example texts
    texts = [
        "I have a problem with my iPhone that needs to be resolved asap!!",
        "The weather will be clear with sunny skies tomorrow",
        "This restaurant's pizza is the best in the city"
    ]
    
    # Different label sets for different scenarios
    label_sets = {
        "urgency": ["urgent", "not urgent"],
        "weather": ["sunny", "rainy", "cloudy", "stormy"],
        "review": ["positive", "negative", "neutral"]
    }
    
    print("\nZero-shot Classification Examples:")
    for text in texts:
        print(f"\nText: {text}")
        # Choose appropriate labels based on the text
        if "problem" in text.lower() or "issue" in text.lower():
            labels = label_sets["urgency"]
        elif "weather" in text.lower():
            labels = label_sets["weather"]
        else:
            labels = label_sets["review"]
            
        result = classifier(text, labels)
        print(f"Labels: {result['labels']}")
        print(f"Scores: {result['scores']}")

if __name__ == "__main__":
    zero_shot_classify()
