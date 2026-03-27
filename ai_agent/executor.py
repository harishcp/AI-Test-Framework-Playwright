import re

def execute_steps(page, step):
    """Execute a single Playwright step on the page"""
    step = step.strip()
    
    if not step:
        return
    
    try:
        if step.startswith("goto("):
            # Extract URL from goto('url')
            match = re.search(r"goto\(['\"](.+?)['\"]\)", step)
            if match:
                url = match.group(1)
                print(f"Navigating to: {url}")
                page.goto(url, wait_until="load")
                page.wait_for_load_state("networkidle")

        elif step.startswith("fill("):
            # Extract selector and value from fill('selector', 'value')
            match = re.search(r"fill\(['\"](.+?)['\"]\s*,\s*['\"](.+?)['\"]\)", step)
            if match:
                selector = match.group(1)
                value = match.group(2)
                print(f"Filling '{selector}' with '{value}'")
                page.wait_for_selector(selector, timeout=10000)
                page.fill(selector, value, timeout=10000)

        elif step.startswith("click("):
            # Extract selector from click('selector') or click(text='text')
            # Handle both click('text=Login') and click(selector)
            match = re.search(r"click\(['\"](.+?)['\"]\)", step)
            if match:
                selector = match.group(1)
                print(f"Clicking: {selector}")
                page.wait_for_selector(selector, timeout=10000)
                page.click(selector, timeout=10000)
    
    except Exception as e:
        print(f"Error executing step '{step}': {e}")
        raise