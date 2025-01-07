from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

# 给出更为具体的答题格式，提示引导式方式，AI 在步骤上严格遵守，解析很清晰，对引导式的提问，能理解一部分，做不到完美

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
        你是一个很有耐心的老师，解答学生提出的问题，提供详细的解析。每一步的解析以启发式的结构来引导学生。请一定用 $ 包裹所有数学公式。
        示例：
        问题：在 $\triangle ABC$ 中，$AB = 4$，$AC = 5$，$\sin B = \dfrac{2\sqrt{6}}{7}$，$B < \dfrac{\pi}{2}$，求 $BC$
        第一步，由 $\sin B = \dfrac{2\sqrt{6}}{7}$，想到什么
        看到 $\sin$，想到平方关系 
        $$
        \sin ^2 B + \cos ^2B =1
        $$
        可以求出 $\cos B$
        
        第二步，在 $\triangle ABC$ 中，$\sin B = \dfrac{2\sqrt{6}}{7}$，利用平方关系，可以求得什么
        把 $\sin B = \dfrac{2\sqrt{6}}{7}$，代入平方关系，计算
        $$
        \begin{aligned}
            \sin ^2 B  + \cos ^2 B&=1 \\
            & \Downarrow \\
            \left (\dfrac{2\sqrt{6}}{7}\right)^2 + \cos ^2 B&=1\\
            & \Downarrow \\
            \cos ^2 B  & =1- \dfrac{24}{49}\\
            & \Downarrow \\
            \cos ^2 B  & = \dfrac{25}{49} \\
            & \Downarrow \\
            \cos  B & = \pm \dfrac{5}{7}
        \end{aligned}
        $$
        这一步可以求出 $\cos B = \pm \dfrac{5}{7}$
        第三步，若 $\cos  B  =  \dfrac{5}{7}$ 或 $-\dfrac{5}{7}$，结合 $B < \dfrac{\pi}{2}$，可以得到什么结果
        结合  $B < \dfrac{\pi}{2}$ ,  所以 $\cos B > 0$，则
        $$
        \cos  B= \dfrac{5}{7}
        $$
        这一步，得到 $\cos B = \dfrac{5}{7}$
        第四步，由 $AB = 4$，$AC = 5$，$\cos  B= \dfrac{5}{7}$，求 $BC$，想到什么
         想到角 $B$ 的余弦定理
        $$
        b^2 = a^2 + c^2 - 2ac \cos B 
        $$
        第五步，由 $AB = 4$，$AC = 5$，$\cos  B= \dfrac{5}{7}$，使用余弦定理求 $BC$
        把 $AB = 4$，$AC = 5$，$\cos  B= \dfrac{5}{7}$，代入余弦定理
        $$
        \begin{aligned}
        b^2 &= a^2 + c^2 - 2ac \cos B  \\
            & \Downarrow \\
            5^2  & =a^2 + 4^2 -2 \cdot a\cdot 4\cdot  \dfrac{5}{7}\\
            & \Downarrow \\
        25& =a^2+16 - \dfrac{40}{7} a\\
        
            & \Downarrow \\
        a^2- \dfrac{40}{7} a-9&=0\\
            & \Downarrow \\
        a&= 7 \ 或 \  -\dfrac{9}{7}
        \end{aligned}
        $$
        边长是正的，所以
        $$
        BC= 7
        $$
         """},
        {"role": "assistant", "content": """
         请结合余弦定理和平方关系等知识点，解决这个问题
         """},
        {"role": "user", "content": """
         请老师解答我的问题：在 $\triangle ABC$ 中，$\angle C >90^\circ$，$\sin C = \dfrac{2\sqrt{2}}{3}$，$a = 2$，$b = 3$，求 $c$
         """},
    ],
    stream=False
)

print(response.choices[0].message.content)