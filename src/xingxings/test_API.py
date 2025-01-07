from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

test_api_key = os.getenv("DEEPSEEK_API_KEY")
test_url = 'https://api.deepseek.com'

client = OpenAI(api_key=test_api_key, base_url= test_url)

# test api

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Who are you?"},
    ],
    stream=False
)

print(response.choices[0].message.content)