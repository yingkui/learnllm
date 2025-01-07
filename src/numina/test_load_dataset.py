from datasets import load_dataset

dataset = load_dataset("AI-MO/aimo-validation-amc", split="train[:10]") 
print(dataset)