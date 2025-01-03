from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# 让 AI 步骤化的回答问题，并按照要求的格式输出

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
        你是一个很有耐心的老师，学生提出一个问题，你要给出步骤化的解析，解析要非常详细，每一步解析包含依据的信号、执行的过程和得到的结果。
         其他要求如下：
         --1. 结果不可以用无限小数表示，如果是无理数，要进行分母有理化。
         --2. 请一定用 $ 展示数学公式，其中 \geq 要写成 \geqslant，\leq 要写成 \leqslant。
         --3. 多行公式请一定用 aligned 进行对齐，下面是关于公式对齐的示例
         示例一：
         $$
         \begin{aligned}
            \sin^2 C + \cos^2 C & = 1 \\
            \sin ^2 & = 1 - \cos^2 C
         \end{aligned}
         $$
         示例二：
         $$
         \begin{aligned}
         \sin ^2 & = 1 - \cos^2 C \\
         & = 1 - (\dfrac{1}{3})^2 \\
         & = 1 - \dfrac{1}{9} \\
         & = \dfrac{8}{9}
         \end{aligned}
         $$
         --4. latex 公式不能有乱码，如果有乱码，请重新回答。
         """},
        {"role": "system", "content": """

         """},
        {"role": "user", "content": """
         请老师解答我的问题：在 $\\triangle ABC$ 中，$a^2 - b^2 + c^2 = 2$，$\sin B = \dfrac{1}{3}$，$B \in (0, \dfrac{\pi}{2})$，求三角形的面积 $S_{\triangle ABC}$
         """}         
    ],
    stream=False,
    temperature= 0.2
)

print(response.choices[0].message.content)

