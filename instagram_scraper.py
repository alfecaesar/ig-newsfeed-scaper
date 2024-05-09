from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver (you can use another browser by changing this)
driver = webdriver.Chrome()

# Open Instagram
driver.get("https://www.instagram.com/")

# Wait for the login fields to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

# Enter your login credentials
username = "*****"
password = "*****"
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)

# Click the login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for the home page to load
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav ul")))

# Capture screenshot of the newsfeed
driver.save_screenshot("instagram_newsfeed.png")

# Get all the posts
posts = driver.find_elements(By.CSS_SELECTOR, "article")

# Iterate through posts
for post in posts:
    # Check if post is sponsored or suggested
    is_sponsored = post.text.startswith("Sponsored")
    is_suggested = post.text.startswith("Suggested for you")
    
    if is_sponsored or is_suggested:
        # Capture screenshot of the sponsored/suggested post
        post.screenshot(f"sponsored_post_{post.id}.png")
        
        # Save link and text content of the sponsored/suggested post
        link = post.find_element(By.TAG_NAME, "a").get_attribute("href")
        text_content = post.text
        
        # Log the details
        print("Sponsored:" if is_sponsored else "Suggested:", link, text_content)

# Close the browser
driver.quit()
