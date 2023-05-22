# Open browser
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)
URL = "https://practicetestautomation.com/practice-test-login/"

# Go to the page
driver.get(URL)
driver.maximize_window()

time.sleep(3)

# Type username student into Username field
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("student")

# Type password Password123 into Password field
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Password123")

# Push Submit button
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')

text_locator_element = driver.find_element(By.CLASS_NAME, "post-title")
actual_text = text_locator_element.text
assert actual_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_button_element = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')
assert logout_button_element.is_displayed()
