from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer


dataset = load_dataset("yelp_review_full")
dataset["train"][100]

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

tokenized_datasets = dataset.map(tokenize_function, batched=True)

small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))


# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=5)
# model = AutoModelForSequenceClassification.from_pretrained("deepseek-ai/DeepSeek-V3", num_labels=5)

training_args = TrainingArguments(output_dir="test_trainer", eval_strategy="epoch")

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset
)

trainer.train()

trainer.evaluate()
0
trainer.predict(small_eval_dataset)