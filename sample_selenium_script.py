
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open browser
driver = webdriver.Chrome()

# 2. Go to login page
driver.get("https://example.com/login")
driver.maximize_window()
time.sleep(2)

# 3. Enter username
driver.find_element(By.NAME, "username").send_keys("testuser")

# 4. Enter password
driver.find_element(By.NAME, "password").send_keys("password123")

# 5. Click login
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# 6. Validate login
time.sleep(3)
if "dashboard" in driver.current_url:
    print("✅ Login successful!")
else:
    print("❌ Login failed.")

# 7. Close browser
driver.quit()
