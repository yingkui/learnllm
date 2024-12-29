from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    pipeline,
)
from datasets import load_dataset, DatasetDict
import torch

# 1. 加载数据集
def load_and_preprocess_data(data_file):
    # 加载 JSON 数据集
    dataset = load_dataset("json", data_files=data_file)

    # 划分训练集和验证集
    dataset = dataset["train"].train_test_split(test_size=0.1)

    # 转换为 DatasetDict 格式
    dataset = DatasetDict({
        "train": dataset["train"],
        "validation": dataset["test"],
    })

    # 预处理数据集：将问题和解答合并为一个连贯的文本序列
    def preprocess_function(examples):
        # 假设字段名是 "instruction" 和 "output"
        text = [f"问题：{q} 解答：{a}" for q, a in zip(examples["instruction"], examples["output"])]
        return {"text": text}

    dataset = dataset.map(preprocess_function, batched=True)
    return dataset

# 2. 数据编码
def encode_data(dataset, tokenizer):
    # 设置 pad_token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token  # 使用 eos_token 作为 pad_token

    def tokenize_function(examples):
        # 对文本序列进行编码
        tokenized = tokenizer(
            examples["text"],
            truncation=True,
            padding="max_length",
            max_length=8,  # 进一步减小序列长度
        )
        tokenized["labels"] = tokenized["input_ids"].copy()  # 将 input_ids 复制为 labels
        return tokenized

    dataset = dataset.map(tokenize_function, batched=True)
    return dataset

# 3. 微调模型
def fine_tune_model(dataset, model_name, output_dir):
    # 加载模型和分词器
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name) # 因果模型

    # 启用梯度检查点
    model.gradient_checkpointing_enable()

    # 编码数据
    dataset = encode_data(dataset, tokenizer)

    # 设置训练参数
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=1,  # 进一步减小批次大小
        per_device_eval_batch_size=1,   # 进一步减小批次大小
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=2,
        save_steps=500,
        logging_dir="./logs",
        logging_steps=10,
        fp16=True,  # 启用混合精度训练
        gradient_accumulation_steps=8,  # 增加梯度累积步数
    )

    # 定义训练器
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        tokenizer=tokenizer,
    )

    # 开始训练
    trainer.train()

    # 保存模型
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"模型已保存到 {output_dir}")

# 4. 使用微调后的模型
def use_fine_tuned_model(model_dir, input_text):
    # 加载微调后的模型
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    # 创建推理管道
    math_solver = pipeline("text-generation", model=model, tokenizer=tokenizer)

    # 使用模型进行推理
    result = math_solver(input_text, max_length=100)
    print("推理结果:", result)

# 主函数
def main():
    # 数据集路径
    data_file = "raw-data/triangle_training_data.json"  # 替换为你的数据集路径
    # 模型名称
    model_name = "model/deepseek-math-7b-instruct"
    # 微调后模型保存路径
    output_dir = "./fine-tuned-model"

    # 加载并预处理数据
    dataset = load_and_preprocess_data(data_file)

    # 微调模型
    fine_tune_model(dataset, model_name, output_dir)

    # 使用微调后的模型进行推理
    input_text = "solve the problem: in triangle ABC, if $\dfrac{a}{b} = 2$, find the value of $\dfrac{\sin^2 A}{\sin^2 B}$"  # 替换为你的输入文本
    use_fine_tuned_model(output_dir, input_text)

if __name__ == "__main__":
    main()