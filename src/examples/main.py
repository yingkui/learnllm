from text_generation import generate_text
from sentiment_analysis import analyze_sentiment
from named_entity_recognition import recognize_entities
from text_summarization import summarize_text
from translation import translate_text
from question_answering import question_answering
from zero_shot_classification import zero_shot_classify
from fill_mask import fill_masks

def run_all_examples():
    print("Running Hugging Face Examples...")
    
    # Basic examples
    generate_text()
    analyze_sentiment()
    recognize_entities()
    summarize_text()
    translate_text()
    
    # Advanced examples
    question_answering()
    zero_shot_classify()
    fill_masks()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    run_all_examples()