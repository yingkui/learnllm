from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# 让 AI 步骤化的回答问题

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
         你是一个很有耐心的老师，解答学生提出的问题，提供一步一步的解析，每一步的解析格式为：依据 [信号]，执行了[操作]，得到了[结果]。
         """},
        {"role": "user", "content": """
         请老师解答我的问题：在 $\triangle ABC$ 中，已知 $\angle A = \dfrac{\pi}{3}$, $a = 3$，求三角形面积的最大值
         """},
    ],
    stream=False
)

print(response.choices[0].message.content)