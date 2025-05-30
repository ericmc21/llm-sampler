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
        "content": "You are an expert software engineer that prefers functional programming.",
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values in a dictionary.",
    },
]

response = generate_response(messages)
print(response)

# We are going to make this verbose so it is clear what
# is going on. In a real application, you would likely
# just append to the messages list.
messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that prefers functional programming.",
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values in a dictionary.",
    },
    # Here is the assistant's response from the previous step
    # with the code. This gives it "memory" of the previous
    # interaction.
    {"role": "assistant", "content": response},
    # Now, we can ask the assistant to update the function
    {"role": "user", "content": "Update the function to include documentation."},
]

response = generate_response(messages)
print(response)
