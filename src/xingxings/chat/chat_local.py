from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# 加载本地模型和分词器
def load_model(model_path, device="cuda" if torch.cuda.is_available() else "cpu"):
    try:
        model = AutoModelForCausalLM.from_pretrained(model_path).to(device) # 因果模型
        # model = AutoModelForSeq2SeqLM.from_pretrained(model_path) # 序列模型
        tokenizer = AutoTokenizer.from_pretrained(model_path)

        # 检查并设置 pad_token
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        print(f"Model and tokenizer loaded successfully on {device}!")
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None

# 生成答案
def generate_answer(model, tokenizer, question, max_length=4096):
    try:
        # 编码输入，包括 attention_mask
        inputs = tokenizer(question, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs["input_ids"].to(model.device)
        attention_mask = inputs["attention_mask"].to(model.device)

        # 检查并设置 pad_token_id
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.eos_token_id

        # 生成答案
        output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            pad_token_id=tokenizer.pad_token_id,
            max_length=max_length
        )

        # 解码输出
        answer = tokenizer.decode(output[0], skip_special_tokens=True)
        return answer
    except Exception as e:
        print(f"Error generating answer: {e}")
        return None

# 主程序
def main():
    # 本地模型路径
    model_path = "./model/deepseek-math-7b-instruct"  # 替换为你的本地路径

    # 加载模型和分词器
    model, tokenizer = load_model(model_path)
    if model is None or tokenizer is None:
        return

    # 用户交互
    print("Welcome to the QA system! Type 'exit' to quit.")
    while True:
        # 获取用户输入
        question = input("\nYour question (or 'exit' to quit): ")
        if question.lower() == "exit":
            break

        # 生成答案
        answer = generate_answer(model, tokenizer, question)
        if answer:
            print(f"\nAnswer: {answer}")
        else:
            print("Failed to generate an answer.")

if __name__ == "__main__":
    main()