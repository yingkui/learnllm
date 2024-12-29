from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
You are a helpful assistant. Output the information in the following format:

| Name       | Age | Occupation    |
|------------|-----|---------------|
| [Name]     | [Age] | [Occupation]|"""},
        {"role": "user", "content": """
Provide the details for these individuals:
1. Alice, 25, Engineer
2. Bob, 30, Teacher
3. Carol, 27, Designer"""},
    ],
    stream=False
)

print(response.choices[0].message.content)