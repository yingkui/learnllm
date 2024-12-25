from transformers import pipeline

def generate_text():
    # Initialize text generation pipeline
    generator = pipeline('text-generation', model='distilgpt2')
    
    # Generate some text
    prompt = "Hello, world! Today I want to"
    generated_text = generator(prompt, max_length=30, num_return_sequences=2)
    
    print("\nText Generation Example:")
    print(f"Prompt: {prompt}")
    print("Generated texts:")
    for i, g in enumerate(generated_text):
        print(f"{i+1}: {g['generated_text']}")

if __name__ == "__main__":
    generate_text()
