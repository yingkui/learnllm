from transformers import pipeline

def summarize_text():
    summarizer = pipeline('summarization')
    long_text = """
    Artificial intelligence has transformed the technology landscape in recent years. 
    Companies are investing heavily in AI research and development. 
    The field continues to evolve with new breakthroughs in machine learning and neural networks.
    Many experts believe that AI will continue to revolutionize industries like healthcare,
    transportation, and education in the coming decades.
    """
    
    summary = summarizer(long_text, max_length=50, min_length=10)
    print("\nText Summarization Example:")
    print(f"Original: {long_text}")
    print(f"Summary: {summary[0]['summary_text']}")

if __name__ == "__main__":
    summarize_text()
