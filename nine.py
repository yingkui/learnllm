from dotenv import load_dotenv
import os
import re  # Import the re module
load_dotenv()

from openai import OpenAI
from anthropic import Anthropic

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

deepseek_client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")
openai_client = OpenAI(api_key=openai_api_key)
anthropic_client = Anthropic()

prompt = '9.9和9.11哪个大'

deepseek_counter = []
openai_counter = []
anthropic_counter = []

for _ in range(50):
    deepseek_response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    deepseek_content = deepseek_response.choices[0].message.content

    # Extract the boxed answer using regex
    match = re.search(r'\\boxed{([^}]*)}', deepseek_content)
    if match:
        boxed_answer = match.group(1)  # Extract content inside \boxed{}
        print(boxed_answer)


for _ in range(0):

    openai_response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(openai_response.choices[0].message.content)


    anthropic_response = anthropic_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(anthropic_response.content[0].text)

