from ai_agent.agent import generate_test_steps
from ai_agent.executor import execute_steps
from utils.browser import start_browser

# tests/test_ai_login.py
def test_ai_login():
    user_input = """
    Go to https://the-internet.herokuapp.com/login
    Enter tomsmith into username
    Enter SuperSecretPassword! into password
    Click login
    """
    steps = generate_test_steps(user_input, use_mock=True)  # Use mock to avoid API call
    assert "goto('https://the-internet.herokuapp.com/login')" in steps