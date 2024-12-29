from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

import json

# Load the JSON file
with open(os.path.join(os.path.dirname(__file__), "json_to_sql.json"), "r") as file:
    data = json.load(file)

# Prepare the input data for the AI model
data_input = "\n".join([f"({row['id']}, '{row['name']}', '{row['role']}')" for row in data])

# Define the prompt
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
You are a helpful assistant. Output the information in the following SQL insert format:

INSERT INTO employees (id, name, role) VALUES
([Value 1], [Value 2], [Value 3]),
...
"""},
        {"role": "user", "content": f"""
Transform the following data into the specified SQL insert format:
{data_input}
"""},
    ],
    stream=False
)

print(response.choices[0].message.content)