import os

def take_screenshot(driver, name):
    path = f"screenshots/{name}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(path)
    return path
