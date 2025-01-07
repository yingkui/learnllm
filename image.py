from openai import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

import base64

# opens the image file in "read binary" mode
with open("./formula.png", "rb") as image_file:

    #reads the contents of the image as a bytes object
    binary_data = image_file.read() 

    #encodes the binary data using Base64 encoding
    base_64_encoded_data = base64.b64encode(binary_data) 

    #decodes base_64_encoded_data from bytes to a string
    base64_string = base_64_encoded_data.decode('utf-8')

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": f"""
        {{
            "type": "image",
            "source": {{
                "type": "base64",
                "media_type": "image/png",
                "data": "{base64_string}"
            }}
        }}
        """}
    ],
    stream=False
)

print(response.choices[0].message.content)

# POSITIVE