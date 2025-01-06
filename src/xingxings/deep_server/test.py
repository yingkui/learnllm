import requests

# 服务器的 URL
url = "http://123.56.244.102:5001/run-python"

# 请求数据
data = {
    "messages": [
        {"role": "system", "content": "你是一个老师，请详细的回答老师的问题"},
        {"role": "user", "content": "请老师解答我的问题：在 $\\triangle ABC$ 中，$a^2 - b^2 + c^2 = 2$，$\\sin B = \\dfrac{1}{3}$，$B \\in (0, \\dfrac{\\pi}{2})$，求三角形的面积 $S_{\\triangle ABC}$"}
    ]
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 打印服务器返回的结果
print(response.json())


# curl -X POST http://123.56.244.102:5001/run-python -H "Content-Type: application/json" -d '{"messages": [{"role": "user", "content": "Hello, DeepSeek!"}]}' {"output":"Hello! How can I assist you today? \ud83d\ude0a"}






