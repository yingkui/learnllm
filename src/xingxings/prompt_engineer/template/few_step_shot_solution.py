from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# 让 AI 步骤化的回答问题，并按照要求的格式输出，在输出的内容上不满足要求时，提供一些思路和指引，供大模型参考，输出想要的结果

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
        下面是关于中线问题的一个示例：
        问题：在三角形 $ABC$ 中，$D$ 是 $AC$ 的中点，$BD$ 是三角形的中线，$B = \dfrac{\pi}{3}$，$b = 2\sqrt{3}$，求中线 $AD$ 的最大值
        这类问题的解决思路如下：
        第一步，看到中线 $BD$，就想到向量关系，用 $\overrightarrow{BA}$ 和 $\overrightarrow{BC}$ 表示 $\overrightarrow{BD}$
        第二步，等式两侧进行平方，得到 $BD$ 的平方和 $a$、$c$ 的关系式
        第三步，对 $B$，$b$，使用余弦定理，得到 $a$、$c$ 的关系
        第四步，结合第二步和第三步的结果，用 $ac$ 表示 $BD$ 的平方 
        第五步，利用第三步的结果，结合基本不等式，求 $ac$ 的最大值
        第六步，利用第五步的结果，可以求出 $BD$ 的最大值
         """},
        {"role": "user", "content": """
         请老师解答我的问题：在三角形 $ABC$ 中，$D$ 是 $BC$ 边上中点，$AD$ 是中线，$A = \dfrac{\pi}{3}$，$a = 2$，求中线 $AD$ 的最大值
         """}
    ],
    stream=False,
    temperature= 0.2
)

print(response.choices[0].message.content)
