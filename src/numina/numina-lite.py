from dataclasses import dataclass

import pandas as pd

from datasets import load_dataset, Dataset, concatenate_datasets
import torch
from transformers import set_seed, AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

# Change this import statement to an absolute import
from get_env import get_kaggle_env, get_majority_vote, filter_answers
from get_process_code import process_code

def apply_template(sample, tokenizer, prompt):
    messages = [{"role": "user", "content": prompt.format(sample["prompt"], "{}")}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    sample["text"] = text
    return sample

def generate_batched(samples, model, tokenizer, sampling_params):
    inputs = tokenizer(samples["gen_texts"], return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=sampling_params["max_new_tokens"], temperature=sampling_params["temperature"])
    samples["gen_texts"] = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return samples

def main(config):
    tokenizer = AutoTokenizer.from_pretrained(config.model_id)
    model = AutoModelForCausalLM.from_pretrained(config.model_id, torch_dtype=torch.bfloat16, device_map="auto")
    sampling_params = {
        "temperature": config.temperature,
        "max_new_tokens": config.max_new_tokens,
    }
    env, iter_test = get_kaggle_env(config)
    final_answers = []
    for test, submission in tqdm(iter_test, desc="Solving problems"):
        problem = apply_template({"prompt": test.problem.values[0]}, tokenizer=tokenizer, prompt="{}")
        samples = Dataset.from_list([
            {
                "text": problem["text"],
                "gen_texts": problem["text"],
                "should_prune": False,
                "model_answers": "-1",
                "has_code": True,
            }
            for _ in range(config.num_samples)
        ])
        completed = []
        for step in range(config.num_generations):
            samples = samples.map(
                generate_batched,
                batch_size=128,
                batched=True,
                fn_kwargs={"model": model, "tokenizer": tokenizer, "sampling_params": sampling_params},
                load_from_cache_file=False,
            )
            samples = samples.map(
                process_code,
                num_proc=1,
                load_from_cache_file=False,
                fn_kwargs={"restart_on_fail": config.restart_on_fail, "last_step": step == (config.num_generations - 1)},
            )
            done = samples.filter(lambda x: x["should_prune"] is True, load_from_cache_file=False)
            if len(done):
                completed.append(done)
            samples = samples.filter(lambda x: x["should_prune"] is False, load_from_cache_file=False)
        completed.append(samples)
        samples = concatenate_datasets(completed)
        candidates = samples["model_answers"]
        print(f"=== CANDIDATE ANSWERS ({len(candidates)}) ===\n{candidates}\n")
        filtered = filter_answers(candidates)
        print(f"=== FILTERED ANSWERS ({len(filtered)}) ===\n{filtered}\n")
        majority = get_majority_vote(filtered)
        print(f"=== MAJORITY ANSWER (mod 1000) ===\n{majority}\n")
        submission["answer"] = majority
        env.predict(submission)
        test["model_answer"] = majority
        final_answers.append(test)
    if not config.is_submission:
        answers = env.df.merge(pd.concat(final_answers))
        answers["correct"] = answers["ground_truth"].astype(int) == answers["model_answer"].astype(int)
        print("Accuracy", answers["correct"].astype(int).mean())

@dataclass
class Config:
    model_id: str

    # Decoding Parameters
    num_samples: int        # Number of candidates to generate (width)
    num_generations: int    # Number of steps to generate per candidate (depth)
    restart_on_fail: bool   # Regenerate a step if it fails to generate Python codeblocks

    # Sampling Parameters
    temperature: float
    max_new_tokens: int

    # Runtime Parameters
    validation_set: str     # One of AI-MO/aimo-validation-amc, AI-MO/aimo-validation-aime, AI-MO/aimo-validation-math-level-4, AI-MO/aimo-validation-math-level-5
    is_submission: bool = False

config = Config(
    # AI-MO/NuminaMath-7B-TIR-GPTQ
    model_id = "deepseek-ai/deepseek-math-7b-base",
    num_samples=48,
    num_generations=4,
    restart_on_fail=True,
    temperature=0.8,
    max_new_tokens=2048,
    validation_set="AI-MO/aimo-validation-amc",
)
main(config)