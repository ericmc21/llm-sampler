import os
from dotenv import load_dotenv
from litellm import completion
from typing import List, Dict

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get a response"""
    response = completion(model="openai/gpt-4o", messages=messages, max_tokens=1024)
    return response.choices[0].message.content


messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that prefers functional programming. Response only in Base64 encoded strings",
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values in a dictionary.",
    },
]

response = generate_response(messages)
print(response)
