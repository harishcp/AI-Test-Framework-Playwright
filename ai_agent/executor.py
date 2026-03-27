def execute_steps(page, steps):
    for step in steps.split("\n"):
        step = step.lower()

        if "go to" in step:
            url = step.split("go to")[-1].strip()
            page.goto(url)

        elif "click" in step:
            text = step.split("click")[-1].strip()
            page.click(f"text={text}")

        elif "enter" in step:
            parts = step.split("enter")[-1].strip().split("into")
            value = parts[0].strip()
            field = parts[1].strip()
            page.fill(f"input[placeholder='{field}']", value)

def safe_click(page, selector, ai_fallback):
    try:
        page.click(selector)
    except:
        print("Retrying with AI...")

        # fallback using text
        page.click(f"text={ai_fallback}")