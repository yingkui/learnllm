import requests

# 模型服务器的地址
url = "http://localhost:1234/v1/chat/completions"

# 请求的 JSON 数据
data = {
    "messages": [
        {
            "role": "user",
            "content": "在 $\triangle ABC$ 中，若 $B = \dfrac{\pi}{3}$，求 $\sin A + \sin C$ 的取值范围"
        }
    ],
    "max_tokens": 512,
    "temperature": 0.7
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 检查响应状态码
if response.status_code == 200:
    # 解析响应 JSON
    result = response.json()
    # 提取生成的文本
    generated_text = result["choices"][0]["message"]["content"]
    print("Generated Text:", generated_text)
else:
    print("Error:", response.status_code, response.text)