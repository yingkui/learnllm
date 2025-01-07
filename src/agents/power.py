from dotenv import load_dotenv
import os
from huggingface_hub import login, HfApi, Repository

load_dotenv()

# Log in using the Hugging Face access token
hf_token = os.getenv("HUGGINGFACE_API_KEY")
if hf_token:
    try:
        user_info = HfApi().whoami(token=hf_token)
        login(token=hf_token)
        # Check access to the gated repository
        repo_url = "meta-llama/Meta-Llama-3.1-8B-Instruct"
        repo = Repository(repo_url, token=hf_token)
        if not repo.has_access():
            print(f"Access to the repository {repo_url} is restricted. Please request access at https://huggingface.co/{repo_url}.")
    except Exception as e:
        print(f"Failed to authenticate with Hugging Face: {e}")
else:
    print("HUGGINGFACE_API_KEY environment variable not set")

from transformers.agents import CodeAgent

agent = CodeAgent(tools=[])
agent.run("What is the result of 2 power 3.7384?")