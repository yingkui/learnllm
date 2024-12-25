from transformers import pipeline

def fill_masks():
    unmasker = pipeline('fill-mask')
    
    # Example masked sentences
    masked_texts = [
        "Paris is the <mask> of France.",
        "The <mask> is the largest planet in our solar system.",
        "Shakespeare wrote many famous <mask> and sonnets."
    ]
    
    print("\nFill-mask Examples:")
    for text in masked_texts:
        print(f"\nOriginal: {text}")
        results = unmasker(text)
        print("Top 5 predictions:")
        for result in results:
            print(f"- {result['token_str']} (score: {result['score']:.3f})")

if __name__ == "__main__":
    fill_masks()