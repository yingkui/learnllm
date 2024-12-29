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
You are a helpful assistant. Output the information in the following JSON format:

{
  "name": "[Name]",
  "age": [Age],
  "occupation": "[Occupation]"
}"""},
        {"role": "user", "content": """
Provide the following information in the specified JSON format:
- Name: Alex Johnson
- Age: 35
- Occupation: Software Engineer"""},
    ],
    stream=False
)

print(response.choices[0].message.content)