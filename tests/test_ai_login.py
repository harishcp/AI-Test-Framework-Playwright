from ai_agent.agent import generate_test_steps
from ai_agent.executor import execute_steps
from utils.browser import start_browser
import os

def test_ai_login():
    user_input = """
    Go to https://the-internet.herokuapp.com/login
    Enter tomsmith into username
    Enter SuperSecretPassword! into password
    Click login
    """

    steps = generate_test_steps(user_input)

    p, browser, page = start_browser()

    # Create folder for screenshots
    os.makedirs("reports/screenshots", exist_ok=True)

    # Execute each step and take screenshot after each
    step_count = 0
    for step in steps:
        if isinstance(step, str) and step.strip():
            step_count += 1
            print(f"\n===== Step {step_count}: {step} =====")
            try:
                # Take screenshot before step
                page.screenshot(path=f"reports/screenshots/step_{step_count}_before.png")
                
                # Execute step
                execute_steps(page, step)
                
                # Take screenshot after step
                page.wait_for_timeout(500)  # Brief pause to ensure rendering
                page.screenshot(path=f"reports/screenshots/step_{step_count}_after.png")
                print(f"Step {step_count} completed successfully")
            except Exception as e:
                print(f"Error in step {step_count}: {e}")
                # Take error screenshot
                page.screenshot(path=f"reports/screenshots/step_{step_count}_error.png")
                raise

    # Final screenshot after test
    page.screenshot(path="reports/screenshots/final.png")

    browser.close()
    p.stop()