from transformers import pipeline

# Initialize a text generation pipeline using a small model
generator = pipeline('text-generation', model='distilgpt2')

# Generate some text
prompt = "Hello, world! Today I want to"
generated_text = generator(prompt, max_length=30, num_return_sequences=1, truncation=True)

# Print the result
print("Generated text:")
print(generated_text[0]['generated_text'])
print(generated_text)