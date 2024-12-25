from transformers import pipeline

def analyze_sentiment():
    sentiment_analyzer = pipeline('sentiment-analysis')
    texts = [
        "I love learning about AI, it's really fascinating!",
        "This movie was terrible and a waste of time.",
        "The weather is okay today, nothing special."
    ]
    
    print("\nSentiment Analysis Examples:")
    for text in texts:
        sentiment = sentiment_analyzer(text)
        print(f"\nText: {text}")
        print(f"Result: {sentiment}")

if __name__ == "__main__":
    analyze_sentiment()
