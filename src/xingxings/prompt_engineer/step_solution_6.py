from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# 要求 AI 对综合问题进行拆解，提出小问题，并给出解析，小问题的颗粒较大，包含了信号翻译、计算执行和结果

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
        你是一个很有耐心的老师，学生提出一个问题，你将这个问题拆分成若干个小问题，引导学生解决几个小问题，从而解决整个大问题，请写出小问题和小问题的解析。请一定用 $ 包裹所有数学公,
         """},
        # {"role": "assistant", "content": """
        #  请结合余弦定理和平方关系等知识点，解决这个问题
        #  """},
        {"role": "user", "content": """
         请老师解答我的问题：在 $\triangle ABC$ 中，$\angle C >90^\circ$，$\sin C = \dfrac{2\sqrt{2}}{3}$，$a = 2$，$b = 3$，求 $c$
         """},
    ],
    stream=False
)

print(response.choices[0].message.content)