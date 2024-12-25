from transformers import pipeline

def question_answering():
    qa_pipeline = pipeline('question-answering')
    
    # Example 1: Simple fact-based QA
    context1 = """
    Hugging Face is an AI company that develops tools for building machine learning applications.
    It was founded in 2016 and has become very popular among AI researchers and developers.
    The company is known for its Transformers library and model hub.
    """
    questions1 = [
        "When was Hugging Face founded?",
        "What is Hugging Face known for?",
        "What kind of company is Hugging Face?"
    ]
    
    print("\nQuestion Answering Examples:")
    for question in questions1:
        answer = qa_pipeline(question=question, context=context1)
        print(f"\nQuestion: {question}")
        print(f"Answer: {answer['answer']}")
        print(f"Confidence: {answer['score']:.4f}")

if __name__ == "__main__":
    question_answering()
