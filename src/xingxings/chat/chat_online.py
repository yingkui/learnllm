# 安装所需的库
# pip install transformers torch

from transformers import pipeline

# 加载模型
# 使用 "text2text-generation" 任务加载 Qwen/Qwen2.5-Math-1.5B 模型
chatbot = pipeline("text2text-generation", model="Qwen/Qwen2.5-Math-1.5B")

# 对话循环
print("开始对话！输入 'exit' 结束对话。")

while True:
    # 获取用户输入
    user_input = input("你: ")
    
    # 如果用户输入 'exit'，结束对话
    if user_input.lower() == "exit":
        print("对话结束。")
        break
    
    # 生成模型回复
    response = chatbot(user_input, max_length=256)  # 增加 max_length 以处理复杂问题
    
    # 提取模型回复内容
    bot_reply = response[0]["generated_text"]
    
    # 打印模型回复
    print(f"AI: {bot_reply}")