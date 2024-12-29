from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": """
You are a knowledgeable assistant who always provides structured, concise, and accurate responses. 
- Format responses as:
  1. Introduction: A short overview.
  2. Key points: Listed in bullet form.
  3. Conclusion: A summary sentence.
- Use a professional tone and avoid unnecessary details.
- Ensure answers are easy to read and understand, even for non-experts."""},
        {"role": "user", "content": """
What is a function in Python?
"""},
    ],
    stream=False
)

print(response.choices[0].message.content)

# 1. **Introduction**:  
# In Python, a function is a reusable block of code designed to perform a specific task. It helps in organizing code, improving readability, and reducing redundancy.

# 2. **Key points**:  
# - Defined using the `def` keyword followed by the function name and parentheses.  
# - Can accept parameters (inputs) and return a value using the `return` statement.  
# - Promotes code reusability and modularity.  
# - Example:  
#   ```python  
#   def greet(name):  
#       return f"Hello, {name}!"  
#   ```  

# 3. **Conclusion**:  
# Functions in Python are essential for structuring code efficiently and performing repetitive tasks with ease.