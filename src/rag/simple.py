# https://huggingface.co/blog/ngxson/make-your-own-rag

import os
from transformers import AutoTokenizer, AutoModel
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# Disable tokenizers parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Ensure the file path is correct
file_path = os.path.join(os.path.dirname(__file__), 'cat-facts.txt')

dataset = []
with open(file_path, 'r') as file:
    dataset = file.readlines()
    print(f'Loaded {len(dataset)} entries')

# Define models
EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'  # Alternative model

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)
model = AutoModel.from_pretrained(EMBEDDING_MODEL)

# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34, 0.21, ...]
VECTOR_DB = []

def add_chunk_to_database(chunk):
    inputs = tokenizer(chunk, return_tensors='pt')
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    VECTOR_DB.append((chunk, embedding))

for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)

# VECTOR_DB gives you [('a line of words', [0.5239096283912659, -0.12007211893796921, 0.08532855659723282, 0.20557759702205658, -0.07963510602712631, 0.020843297243118286, 0.03201184794306755, 0.061384208500385284, -0.15168927609920502, 0.0825481042265892 ... 384 entries])]

def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])
    norm_a = sum([x ** 2 for x in a]) ** 0.5
    norm_b = sum([x ** 2 for x in b]) ** 0.5
    return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
    inputs = tokenizer(query, return_tensors='pt')
    outputs = model(**inputs)
    query_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    # temporary list to store (chunk, similarity) pairs
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((chunk, similarity))
    # sort by similarity in descending order, because higher similarity means more relevant chunks
    similarities.sort(key=lambda x: x[1], reverse=True)
    # finally, return the top N most relevant chunks
    return similarities[:top_n]

input_query = input('Ask me a question: ')
retrieved_knowledge = retrieve(input_query)

print('Retrieved knowledge:')
for chunk, similarity in retrieved_knowledge:
    print(f' - (similarity: {similarity:.2f}) {chunk}')

instruction_prompt = f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}
'''

print(instruction_prompt)

# Generate response using the DeepSeek API
start_time = time.time()
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": instruction_prompt},
        {"role": "user", "content": input_query},
    ],
    stream=False
)
end_time = time.time()

# Print the response from the chatbot
print('Chatbot response:')
print(response.choices[0].message.content)

print(f'Time taken: {end_time - start_time} seconds')