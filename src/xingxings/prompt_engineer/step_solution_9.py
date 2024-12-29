from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# 除了 6 的要求外，要求对公式进行对齐，两个示例的情况下，AI 完美的理解

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
        你是一个很有耐心的老师，学生提出一个问题，你将这个问题拆分成若干个小问题，小问题要足够的简单，通过引导学生解决足够的小问题，从而解决整个大问题，请写出小问题、小问题的四个选项和小问题的解析，小问题应该诱导式的，根据[信号]应该想到什么，四个选项中包含一个正确的，三个错误的,解析要包含执行的[过程]和得到的[结果]，结果要记得分母有理化。
         请一定用 $ 包裹所有数学公式，多行公式请一定用 aligned 进行对齐，下面是关于对齐的示例：
         使用三角函数恒等式
         $$
         \begin{aligned}
            \sin^2 C + \cos^2 C & = 1 \\
            \sin ^2 & = 1 - \cos^2 C
         \end{aligned}
         $$
         代入 $\cos C = \dfrac{1}{3}$，可得
         $$
         \begin{aligned}
         \sin ^2 & = 1 - \cos^2 C \\
         & = 1 - (\dfrac{1}{3})^2 \\
         & = 1 - \dfrac{1}{9} \\
         & = \dfrac{8}{9}
         \end{aligned}
         $$
         """},
        # {"role": "assistant", "content": """
        #  请结合余弦定理和三角函数恒等式等知识点，解决这个问题
        #  """},
        {"role": "user", "content": """
         请老师解答我的问题：在 $\triangle ABC$ 中，$a^2 - b^2 + c^2 = 2$，$\sin B = \dfrac{1}{3}$，$B \in (0, \dfrac{\pi}{2})$，求三角形的面积 $S_{\triangle ABC}$
         """},
    ],
    stream=False
)

print(response.choices[0].message.content)