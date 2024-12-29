from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "在 $\triangle ABC$ 中，若 $\dfrac{a}{b} = 2$，求 $\dfrac{\sin^2 A}{\sin^2 B}$ 的值"},
    ],
    stream=False
)

print(response.choices[0].message.content)