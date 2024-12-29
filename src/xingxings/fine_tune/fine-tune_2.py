from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    TrainingArguments,
    Trainer,
    pipeline,
    AutoModelForCausalLM,
)
from datasets import load_dataset, DatasetDict
import torch

# 1. 加载数据集
def load_and_preprocess_data(data_file):
    dataset = load_dataset("json", data_files=data_file)
    dataset = dataset["train"].train_test_split(test_size=0.1)
    dataset = DatasetDict({
        "train": dataset["train"],
        "validation": dataset["test"],
    })

    def preprocess_function(examples):
        inputs = [f"问题：{q}" for q in examples["instruction"]]
        targets = [f"{a}" for a in examples["output"]]
        return {"input": inputs, "target": targets}

    dataset = dataset.map(preprocess_function, batched=True)
    return dataset

# 2. 数据编码
def encode_data(dataset, tokenizer):
    def tokenize_function(examples):
        model_inputs = tokenizer(
            examples["input"],
            max_length=128,
            truncation=True,
            padding="max_length",
        )
        labels = tokenizer(
            examples["target"],
            max_length=128,
            truncation=True,
            padding="max_length",
        )
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    dataset = dataset.map(tokenize_function, batched=True)
    return dataset

# 3. 微调模型
def fine_tune_model(dataset, model_name, output_dir):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_name) # 序列模型

    # 编码数据
    dataset = encode_data(dataset, tokenizer)

    # 设置训练参数
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=2,
        save_steps=500,
        logging_dir="./logs",
        logging_steps=10,
        fp16=True,  # 启用混合精度训练
        gradient_accumulation_steps=4,  # 增加梯度累积步数
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
    # model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    math_solver = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    result = math_solver(input_text, max_length=4096)
    print("推理结果:", result)

# 主函数
def main():
    data_file = "raw-data/ai_training_data.json"
    model_name = "Qwen/Qwen2.5-Math-1.5B"  # 替换为你的模型名称
    output_dir = "./fine-tuned-model"

    # dataset = load_and_preprocess_data(data_file)
    # fine_tune_model(dataset, model_name, output_dir)

    input_text = "在 $\triangle ABC$ 中，角化边，$\cos C = ?$"
    use_fine_tuned_model(output_dir, input_text)

if __name__ == "__main__":
    main()