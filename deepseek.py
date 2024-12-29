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
        {"role": "user", "content": "什么是余弦定理"},
    ],
    stream=False
)

print(response.choices[0].message.content)

# 余弦定理（Law of Cosines）是三角学中的一个重要定理，用于计算任意三角形中的边长或角度。它适用于所有类型的三角形，包括锐角三角形、直角三角形和钝角三角形。

# 余弦定理的公式如下：

# \[
# c^2 = a^2 + b^2 - 2ab \cos C
# \]

# 其中：
# - \( a \)、\( b \)、\( c \) 分别是三角形的三条边；
# - \( C \) 是边 \( c \) 所对的角。