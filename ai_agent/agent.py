import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HF_API_KEY")


def call_llm(prompt):
    # Use the new Hugging Face router endpoint
    url = "https://router.huggingface.co/models/google/flan-t5-large"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.post(url, headers=headers, json={"inputs": prompt})

    try:
        data = response.json()
    except ValueError:
        raise Exception(f"Invalid JSON response: {response.text}")

    # Check if API returned an error
    if isinstance(data, dict) and "error" in data:
        raise Exception(f"Hugging Face API error: {data['error']}")

    if isinstance(data, list) and "generated_text" in data[0]:
        return data[0]["generated_text"]

    raise Exception(f"Unexpected API response format: {data}")

# ai_agent/agent.py
def generate_test_steps(user_input, use_mock=True):
    if use_mock:
        # Mocked Playwright steps
        return [
            "goto('https://the-internet.herokuapp.com/login')",
            "fill('#username', 'tomsmith')",
            "fill('#password', 'SuperSecretPassword!')",
            "click('text=Login')"
        ]

    prompt = f"""
    Convert this into Playwright test steps:
    {user_input}
    """
    return call_llm(prompt)