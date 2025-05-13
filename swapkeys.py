import os
from dotenv import load_dotenv
import json
from litellm import completion
from typing import List, Dict

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get a response"""
    response = completion(model="openai/gpt-4o", messages=messages, max_tokens=1024)
    return response.choices[0].message.content


code_spec = {
    "name": "swap_keys_values",
    "description": "Swaps the keys and values in a given dictionary",
    "params": {"d": "A dictionary with unique values."},
}

messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that writes clean functional code. You always document your functions",
    },
    {"role": "user", "content": f"Please implement {json.dumps(code_spec)}"},
]

# response = generate_response(messages)
print(json.dumps(code_spec))
