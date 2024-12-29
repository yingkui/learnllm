from datasets import load_dataset

# 加载数据集
data_file = "raw-data/ai_training_data.json"  # 替换为你的数据集路径
dataset = load_dataset("json", data_files=data_file)

# 打印数据集信息
print(dataset)

# 打印第一条数据
print(dataset["train"][0])

# 预处理函数
def preprocess_function(examples):
    # 将 instruction 和 output 合并为一个连贯的文本序列
    text = [f"问题：{q} 解答：{a}" for q, a in zip(examples["instruction"], examples["output"])]
    return {"text": text}

# 预处理数据集

the = preprocess_function(dataset['train'])

# 打印预处理后的第一条数据
print(the['text'][0])