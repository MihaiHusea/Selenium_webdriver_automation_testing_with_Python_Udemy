import pytest
from selenium.webdriver.common.by import By

url = "https://practicetestautomation.com/practice-test-login/"


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        # Go to the page
        driver.get(url)
        driver.maximize_window()

        # Type username student into Username field
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("student")

        # Type password Password123 into Password field
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("Password123")

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button.click()

        # Verify new page URL contains "practicetestautomation.com/logged-in-successfully/"
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')

        text_locator_element = driver.find_element(By.CLASS_NAME, "post-title")
        actual_text = text_locator_element.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        logout_button_element = driver.find_element(By.XPATH,
                                                    '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')
        assert logout_button_element._is_displayed()
