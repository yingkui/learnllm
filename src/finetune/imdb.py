from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
# from transformers import AutoTokenizer, AutoForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset
dataset = load_dataset("imdb")

# Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3")
# model = AutoModelForSequenceClassification.from_pretrained("deepseek-ai/DeepSeek-V3", num_labels=2)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Tokenize data
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
tokenized_datasets = tokenized_datasets.remove_columns(["text"])
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
tokenized_datasets.set_format("torch")

# Split dataset
train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(2000))  # Subsample for speed
test_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(500))

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Trainer API
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Train model
trainer.train()

# Evaluate model
trainer.evaluate()
